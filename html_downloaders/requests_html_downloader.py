import requests
from core.html_downloader import HTMLDownloader


class RequestsHTMLDownloader(HTMLDownloader):
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
    html_downloader = RequestsHTMLDownloader(requests.configs)
    html_downloader.get_html("https://google.com")


if __name__ == "__main__":
    __main()
