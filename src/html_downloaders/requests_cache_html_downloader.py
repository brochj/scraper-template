import requests_cache
from src.core.html_downloader import HTMLDownloader


class RequestsCacheHTMLDownloader(HTMLDownloader):
    def __init__(self, configs, cache_filename: str) -> None:
        self.configs = configs
        self.cache_filename = cache_filename
        self.cache_directory = self.configs.get("cacheDir") + cache_filename

    def get_html(self, url: str) -> str:
        session = requests_cache.CachedSession(self.cache_directory)
        html_downloaded = session.get(url)
        return html_downloaded.text


def __main():
    # Just for testing
    import lib.config_section_reader as cfg

    requests = cfg.ConfigSectionReader(
        "./configs/html_downloaders.ini", "RequestsCache"
    )
    html_downloader = RequestsCacheHTMLDownloader(requests.configs, "tests")
    html_downloader.get_html("https://google.com")


if __name__ == "__main__":
    __main()
