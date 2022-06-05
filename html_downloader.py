from abc import ABC, abstractmethod
import requests


class HTMLDownloader(ABC):
    """Download a HTML from an url"""

    @abstractmethod
    def get_html(self, url: str) -> str:
        pass


class Requests(HTMLDownloader):
    def __init__(self, configs) -> None:
        self.configs = configs

    def get_html(self, url: str) -> str:
        headers: dict = {"User-Agent": self.configs.get("userAgent")}
        html_downloaded = requests.get(url, headers)
        return html_downloaded.text


def __main():
    # Just for testing
    import lib.config_section_reader as cfg

    requests = cfg.ConfigSectionReader("./configs/html_downloaders.ini", "Requests")
    html_downloader = Requests(requests.configs)
    html_downloader.get_html("https://google.com")


if __name__ == "__main__":
    __main()
