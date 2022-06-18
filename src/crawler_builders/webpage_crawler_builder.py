import lib.config_section_reader as cfg
from src.core.crawler_builder import CrawlerBuilder
from src.crawlers.webpage_crawler import WebpageCrawler
from src.html_downloaders.requests_cache_html_downloader import (
    RequestsCacheHTMLDownloader,
)
from src.html_parsers.beautiful_soup_html_parser import BeautifulSoupHTMLParser
from src.output_writers.webpage_sqlite import WebpageSqlite
from src.scrapers.webpage_scraper import WebpageScraper


class WebpageCrawlerBuilder(CrawlerBuilder):
    def build_configurations(self):
        CONFIG_PATH = "./configs/html_downloaders.ini"
        CONFIG_SECTION = "RequestsCache"
        self.configs = cfg.ConfigSectionReader(CONFIG_PATH, CONFIG_SECTION)
        print("Lendo Configuracoes")
        return self

    def build_html_downloader(self):
        CACHE_DB_NAME = "webpage"
        self.html_downloader = RequestsCacheHTMLDownloader(
            self.configs.configs, CACHE_DB_NAME
        )
        print("Criando o html downloader")
        return self

    def build_html_parser(self):
        self.html_parser = BeautifulSoupHTMLParser()
        print("Criando o html parser")
        return self

    def build_scraper(self):
        self.webpage_scraper = WebpageScraper()
        return self

    def build_output_writer(self):
        CONFIG_PATH = "./configs/outputs.ini"
        CONFIG_SECTION = "WebpageSqlite"
        configs = cfg.ConfigSectionReader(CONFIG_PATH, CONFIG_SECTION)
        self.output_writer = WebpageSqlite("webpage.db", configs.configs)
        return self

    def get_result(self) -> WebpageCrawler:
        return WebpageCrawler(
            self.html_downloader,
            self.html_parser,
            self.webpage_scraper,
            self.output_writer,
        )
