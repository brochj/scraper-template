from src.core.crawler import Crawler
from src.html_downloaders.requests_cache_html_downloader import (
    RequestsCacheHTMLDownloader,
)
from src.html_parsers.beautiful_soup_html_parser import BeautifulSoupHTMLParser
from src.output_writers.webpage_sqlite import WebpageSqlite
from src.scrapers.webpage_scraper import WebpageScraper


class WebpageCrawler(Crawler):
    def __init__(
        self,
        html_downloader: RequestsCacheHTMLDownloader,
        html_parser: BeautifulSoupHTMLParser,
        scraper: WebpageScraper,
        output_writer: WebpageSqlite,
    ) -> None:
        self.html_downloader = html_downloader
        self.html_parser = html_parser
        self.webpage_scraper = scraper
        self.output_writer = output_writer

    def crawl(self, url: str):
        html_downloaded = self.html_downloader.get_html(url)
        parsed_html = self.html_parser.parse_html(html_downloaded)
        webpage_model = self.webpage_scraper.scrape(parsed_html, url)
        self.output_writer.save(webpage_model)
