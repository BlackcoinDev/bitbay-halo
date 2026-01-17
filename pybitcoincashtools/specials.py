import sys

is_python2 = sys.version_info.major == 2

if sys.version_info.major < 3:
    from .py2specials import (
        bin_dbl_sha256,
        bin_to_b58check,
        bytes_to_hex_string,
        changebase,
        decode,
        encode,
        from_byte_to_int,
        from_int_representation_to_bytes,
        from_int_to_byte,
        from_string_to_bytes,
        get_code_string,
        is_hexilified,
        lpad,
        random_string,
        safe_from_hex,
        safe_hexlify,
    )

else:
    from .py3specials import (
        bin_dbl_sha256,
        bin_to_b58check,
        bytes_to_hex_string,
        changebase,
        decode,
        encode,
        from_byte_to_int,
        from_int_representation_to_bytes,
        from_int_to_byte,
        from_string_to_bytes,
        get_code_string,
        is_hexilified,
        lpad,
        random_string,
        safe_from_hex,
        safe_hexlify,
    )


def _get_constants():
    if sys.version_info.major < 3:
        from .py2specials import int_types, string_or_bytes_types, string_types

        return string_types, string_or_bytes_types, int_types
    else:
        from .py3specials import int_types, string_or_bytes_types, string_types

        return string_types, string_or_bytes_types, int_types


string_types, string_or_bytes_types, int_types = _get_constants()

__all__ = [
    "bin_dbl_sha256",
    "lpad",
    "get_code_string",
    "changebase",
    "bin_to_b58check",
    "bytes_to_hex_string",
    "safe_from_hex",
    "from_int_representation_to_bytes",
    "from_int_to_byte",
    "from_byte_to_int",
    "from_string_to_bytes",
    "safe_hexlify",
    "encode",
    "decode",
    "random_string",
    "is_hexilified",
    "string_types",
    "string_or_bytes_types",
    "int_types",
]
