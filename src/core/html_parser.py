from abc import ABC, abstractmethod
from typing import Any


class HTMLParser(ABC):
    """Download a HTML from an url"""

    @abstractmethod
    def parse_html(self, html: str) -> Any:
        pass
