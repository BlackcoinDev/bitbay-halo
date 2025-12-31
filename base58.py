import hashlib

# Python 3 refactored base58 module
__b58chars = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
__b58base = len(__b58chars)

def b58encode(v):
    """ encode v, which is bytes, to base58 string. """
    if isinstance(v, str):
        v = v.encode('ascii')

    long_value = 0
    for (i, c) in enumerate(v[::-1]):
        long_value += (256**i) * c

    result = ''
    while long_value >= __b58base:
        div, mod = divmod(long_value, __b58base)
        result = __b58chars[mod] + result
        long_value = div
    result = __b58chars[long_value] + result

    # Bitcoin leading-zero-compression
    nPad = 0
    for c in v:
        if c == 0: nPad += 1
        else: break

    return (__b58chars[0] * nPad) + result

def b58decode(v, length):
    """ decode v (string) into bytes. """
    if isinstance(v, bytes):
        v = v.decode('ascii')
        
    long_value = 0
    for (i, c) in enumerate(v[::-1]):
        long_value += __b58chars.find(c) * (__b58base**i)

    result = bytearray()
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result.append(mod)
        long_value = div
    result.append(long_value)
    
    result = bytes(result[::-1])

    nPad = 0
    for c in v:
        if c == __b58chars[0]: nPad += 1
        else: break

    result = bytes([0]*nPad) + result
    
    if length is not None and len(result) != length:
        return None
    return result

def get_bcaddress_version(strAddress):
    """ Returns None if strAddress is invalid. Otherwise returns integer version of address. """
    addr = b58decode(strAddress, 25)
    if addr is None: return None
    version = addr[0]
    checksum = addr[-4:]
    vh160 = addr[:-4]
    
    h3 = hashlib.sha256(hashlib.sha256(vh160).digest()).digest()
    
    if h3[0:4] == checksum:
        return version
    return None

if __name__ == '__main__':
    # Test case
    assert get_bcaddress_version('15VjRaDX9zpbA8LVnbrCAFzrVzN7ixHNsC') == 0
    _ohai = b'o hai'
    _tmp = b58encode(_ohai)
    assert _tmp == 'DYB3oMS'
    assert b58decode(_tmp, 5) == _ohai
    print("Tests passed")
