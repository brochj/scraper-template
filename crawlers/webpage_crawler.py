import lib.config_section_reader as cfg
from core.crawler_builder import CrawlerBuilder
from html_downloaders.requests_cache_html_downloader import RequestsCacheHTMLDownloader
from html_parsers.beautiful_soup_html_parser import BeautifulSoupHTMLParser
from scrapers.webpage_scraper import WebpageScraper


class WebpageCrawler(CrawlerBuilder):
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
        return self

    def get_result(self):
        self.webpage_scraper = WebpageScraper()
        return self

    def crawl(self, url: str):
        html_downloaded = self.html_downloader.get_html(url)
        parsed_html = self.html_parser.parse_html(html_downloaded)
        return self.webpage_scraper.scrape(parsed_html, url)