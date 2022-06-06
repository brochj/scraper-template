from abc import ABC, abstractmethod


class CrawlerBuilder(ABC):
    @abstractmethod
    def build_configurations(self):
        """Get the necessary configurantion values"""

    @abstractmethod
    def build_html_downloader(self):
        """Create the html Downloader"""

    @abstractmethod
    def build_html_parser(self):
        """Create the html parser"""

    @abstractmethod
    def build_scraper(self):
        """Create the scraper"""

    @abstractmethod
    def get_result(self):
        "Return the final crawler"

    @abstractmethod
    def crawl(self):
        "Return the model populated"
