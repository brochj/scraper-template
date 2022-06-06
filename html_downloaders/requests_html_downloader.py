import requests
from core.html_downloader import HTMLDownloader


class RequestsHTMLDownloader(HTMLDownloader):
    def __init__(self, configs) -> None:
        self.configs = configs

    def get_html(self, url: str) -> str:
        headers: dict = {"User-Agent": self.configs.get("userAgent")}
        html_downloaded = requests.get(url, headers)
        return html_downloaded.text
