# stepic - Python image steganography
# Copyright (C) 2007 Lenny Domnitser
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""Python image steganography

Stepic hides arbitrary data inside PIL images.

Stepic uses the Python Image Library
(apt: python-imaging, web: <http://www.pythonware.com/products/pil/>).
"""

__author__ = "Lenny Domnitser <http://domnit.org/>"
__version__ = "0.3"


import warnings
from typing import Any, Iterable, Iterator, Tuple

try:
    import PIL
except ImportError:
    warnings.warn("Could not find PIL. Only encode_imdata and decode_imdata will work.", ImportWarning, stacklevel=2)
else:
    del PIL


__all__ = ("encode_imdata", "encode_inplace", "encode", "decode_imdata", "decode", "Steganographer")


def encode_imdata(imdata: Iterable[Tuple[int, int, int]], data: bytes) -> Iterator[Tuple[int, int, int]]:
    """given a sequence of pixels, returns an iterator of pixels with
    encoded data"""
    datalen = len(data)
    if datalen == 0:
        raise ValueError("data is empty")

    # Defensive: Check capacity if possible (imdata is often a list due to getdata() behavior in simple usage)
    # If strictly an iterator, we can't check without consuming.
    # But for standard PIL usage, we can try.
    # Note: 3 pixels encode 1 byte (each pixel has 3 colors, we use 3 bits per pixel? No.)
    # The logic:
    # 3 pixels * 3 values = 9 values.
    # Byte (8 bits) + 1 control bit = 9 bits.
    # So 3 pixels are needed for 1 byte of data.

    if hasattr(imdata, "__len__"):
        # cast to Any because mypy/pyright strict might complain about Sized check on generic Iterable
        # strict: we know it likely has len if it came from getdata() but getdata returns a flattened sequence-like
        # actually getdata() returns a sequence object.
        # Strict calculation: datalen * 3 pixels per byte vs total pixels.
        required_pixels = datalen * 3
        if len(imdata) < required_pixels:  # type: ignore
            raise ValueError(f"Image too small. Required {required_pixels} pixels, got {len(imdata)}")  # type: ignore

    imdata_iter = iter(imdata)

    for i in range(datalen):
        pixels = [value & ~1 for value in list(next(imdata_iter)[:3] + next(imdata_iter)[:3] + next(imdata_iter)[:3])]

        item = data[i]
        byte = item

        for j in range(7, -1, -1):
            pixels[j] |= byte & 1
            byte >>= 1
        if i == datalen - 1:
            pixels[-1] |= 1

        # Explicitly yield empty tuples to satisfy strict typing of Tuple[int, int, int]
        # Slicing would be Tuple[int, ...]
        yield (pixels[0], pixels[1], pixels[2])
        yield (pixels[3], pixels[4], pixels[5])
        yield (pixels[6], pixels[7], pixels[8])


def encode_inplace(image: Any, data: bytes) -> None:
    """hides data in an image"""

    # Enforce RGB to match 3-tuple expectation of encode_imdata
    if image.mode != "RGB":
        # Note: convert returns a copy, it doesn't modify inplace unless we assign.
        # But this function is encode_inplace...
        # If user passes non-RGB, and we act inplace, we effectively fail if we don't modify the object.
        # But we can't change the mode of an object inplace easily in PIL without re-assigning logic usually handles copies.
        # However, we can raise an error if not RGB.
        # Given "Practical fixes", enforcing RGB input is safer.
        raise ValueError(f"Image mode {image.mode} not supported. Please convert to RGB.")

    w = image.size[0]
    (x, y) = (0, 0)
    # image.getdata() returns Sequence-like.
    for pixel in encode_imdata(image.getdata(), data):
        image.putpixel((x, y), pixel)
        if x == w - 1:
            x = 0
            y += 1
        else:
            x += 1


def encode(image: Any, data: bytes) -> Any:
    """generates an image with hidden data, starting with an existing
    image and arbitrary data"""

    image = image.copy()
    if image.mode != "RGB":
        image = image.convert("RGB")
    encode_inplace(image, data)
    return image


def decode_imdata(imdata: Iterable[Tuple[int, int, int]]) -> Iterator[bytes]:
    """Given a sequence of pixels, returns an iterator of characters
    encoded in the image"""

    imdata_iter = iter(imdata)
    while True:
        try:
            # We need 3 pixels.
            p1 = next(imdata_iter)
            p2 = next(imdata_iter)
            p3 = next(imdata_iter)
        except StopIteration:
            break

        pixels = list(p1[:3] + p2[:3] + p3[:3])
        byte = 0
        for c in range(7):
            byte |= pixels[c] & 1
            byte <<= 1
        byte |= pixels[7] & 1

        # In Py3, standardizing on bytes return would be best, but legacy might expect str
        # For now, yield bytes to ensure binary data isn't mangled by decoding
        yield bytes([byte])

        if pixels[-1] & 1:
            break


def decode(image: Any) -> bytes:
    """extracts data from an image"""
    # Joining bytes
    return b"".join(decode_imdata(image.getdata()))


class Steganographer:
    "deprecated"

    def __init__(self, image: Any) -> None:
        super().__init__()
        self.image = image
        warnings.warn("Steganographer class is deprecated, and will be removed before 1.0", DeprecationWarning, stacklevel=2)

    def encode(self, data: bytes) -> Any:
        return encode(self.image, data)

    def decode(self) -> bytes:
        return decode(self.image)
