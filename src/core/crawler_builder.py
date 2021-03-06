from abc import ABC, abstractmethod

from src.core.crawler import Crawler


class CrawlerBuilder(ABC):
    @abstractmethod
    def build_configurations(self):
        """Get the necessary configurantion values"""
        return self

    @abstractmethod
    def build_html_downloader(self):
        """Create the html Downloader"""
        return self

    @abstractmethod
    def build_html_parser(self):
        """Create the html parser"""
        return self

    @abstractmethod
    def build_scraper(self):
        """Create the scraper"""
        return self

    @abstractmethod
    def build_output_writer(self):
        """Create the output writer"""
        return self

    @abstractmethod
    def get_result(self) -> Crawler:
        "Return the final crawler"
        return self
