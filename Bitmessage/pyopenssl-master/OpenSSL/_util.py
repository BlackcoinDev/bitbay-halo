from cryptography.hazmat.bindings.openssl.binding import Binding

binding = Binding()
ffi = binding.ffi
lib = binding.lib


def exception_from_error_queue(exceptionType):
    def text(charp):
        if not charp or charp == ffi.NULL:
            return ""
        return native(ffi.string(charp))

    errors = []
    while True:
        error = lib.ERR_get_error()
        if error == 0:
            break
        errors.append(
            (
                text(lib.ERR_lib_error_string(error)),
                text(lib.ERR_func_error_string(error)),
                text(lib.ERR_reason_error_string(error)),
            )
        )

    raise exceptionType(errors)


def native(s):
    """
    Convert :py:class:`bytes` or :py:class:`str` to the native
    :py:class:`str` type, using UTF-8 encoding if conversion is necessary.

    :raise UnicodeError: The input string is not UTF-8 decodeable.

    :raise TypeError: The input is neither :py:class:`bytes` nor
        :py:class:`str`.
    """
    if not isinstance(s, (bytes, str)):
        raise TypeError("%r is neither bytes nor unicode" % s)
    if isinstance(s, bytes):
        return s.decode("utf-8")
    return s


def byte_string(s):
    return s.encode("charmap")
