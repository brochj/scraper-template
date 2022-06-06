from abc import ABC, abstractmethod


class HTMLDownloader(ABC):
    """Download a HTML from an url"""

    @abstractmethod
    def get_html(self, url: str) -> str:
        pass
