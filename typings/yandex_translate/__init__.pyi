"""
Manual type stub for yandex_translate
"""


from typing import Any, Dict, List


class YandexTranslate:

    def __init__(self, key: str) -> None:
        ...

    def translate(self, text: str, lang: str) -> Dict[str, Any]:
        ...

    def detect(self, text: str) -> str:
        ...

    def dirs(self) -> List[str]:
        ...
