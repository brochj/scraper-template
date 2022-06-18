from src.core.crawler import Crawler
from src.core.crawler_builder import CrawlerBuilder


class Director:
    """Responsible for construct a crawler"""

    @staticmethod
    def construct(crawler_builder: CrawlerBuilder) -> Crawler:
        return (
            crawler_builder.build_configurations()
            .build_html_downloader()
            .build_html_parser()
            .build_output_writer()
            .build_scraper()
            .get_result()
        )
