"""
Manual type stub for mechanize (self-contained)
"""


from typing import Any, List, Optional, Union


class Browser:

    def __init__(
        self,
        history: Any = ...,
        request_class: Any = ...,
        content_parser: Any = ...,
        factory_class: Any = ...,
        allow_handle_robots: bool = ...,
        allow_handle_equiv: bool = ...,
        allow_handle_refresh: bool = ...,
        allow_handle_referer: bool = ...,
        allow_handle_redirect: bool = ...,
        allow_handle_gzip: bool = ...,
    ) -> None:
        ...

    def open(self, url: Union[str, Any], data: Any = ..., timeout: Any = ...) -> Any:
        ...

    def follow_link(self, link: Any = ..., nr: int = ..., **kwargs: Any) -> Any:
        ...

    def select_form(self, name: str = ..., predicate: Any = ..., nr: int = ..., **kwargs: Any) -> None:
        ...

    def submit(self, label: str = ..., *args: Any, **kwargs: Any) -> Any:
        ...

    def back(self, n: int = ...) -> None:
        ...

    def reload(self) -> Any:
        ...

    def response(self) -> Any:
        ...

    def geturl(self) -> str:
        ...

    def info(self) -> Any:
        ...

    def code(self) -> int:
        ...

    def get_header(self, header_name: str, default: Any = ...) -> Any:
        ...

    def set_handle_equiv(self, handle: bool) -> None:
        ...

    def set_handle_gzip(self, handle: bool) -> None:
        ...

    def set_handle_redirect(self, handle: bool) -> None:
        ...

    def set_handle_referer(self, handle: bool) -> None:
        ...

    def set_handle_refresh(self, handle: bool) -> None:
        ...

    def set_handle_robots(self, handle: bool) -> None:
        ...

    def set_debug_http(self, handle: bool) -> None:
        ...

    def set_debug_redirects(self, handle: bool) -> None:
        ...

    def set_debug_responses(self, handle: bool) -> None:
        ...

    def addheaders(self, headers: List[Any]) -> None:
        ...

    def set_proxies(self, proxies: Any) -> None:
        ...

    def add_password(self, url: str, user: str, password: str, realm: Optional[str] = ...) -> None:
        ...

    def add_proxy_password(self, user: str, password: str, host: str = ..., realm: Optional[str] = ...) -> None:
        ...

    @property

    def form(self) -> Any:
        ...

    def links(self, **kwargs: Any) -> Any:
        ...

    def forms(self) -> List[Any]:
        ...


class Request:

    def __init__(self, url: str, data: Any = ..., headers: Any = ..., origin_req_host: Any = ..., unverifiable: bool = ...) -> None:
        ...

    def add_header(self, key: str, val: str) -> None:
        ...


class CookieJar:

    def __init__(self, policy: Any = ...) -> None:
        ...

    def extract_cookies(self, response: Any, request: Any) -> None:
        ...

    def add_cookie_header(self, request: Any) -> None:
        ...


class CookiePolicy:
    ...


class DefaultCookiePolicy(CookiePolicy):
    ...


class FileCookieJar(CookieJar):
    ...


class MozillaCookieJar(FileCookieJar):
    ...


class LWPCookieJar(FileCookieJar):
    ...


class LoadError(Exception):
    ...


def urlopen(url: Union[str, Any], data: Any = ..., timeout: Any = ...) -> Any:
    ...

# Common constants and exceptions


class LinkNotFoundError(Exception):
    ...


class FormNotFoundError(Exception):
    ...


class BrowserStateError(Exception):
    ...
