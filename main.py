import os

# Just for testing
import lib.config_section_reader as cfg
from core.director import Director
from crawlers.webpage_crawler import WebpageCrawler
from html_downloaders.requests_cache_html_downloader import RequestsCacheHTMLDownloader
from html_downloaders.requests_html_downloader import RequestsHTMLDownloader
from html_parsers.beautiful_soup_html_parser import BeautifulSoupHTMLParser
from models.webpage import Webpage
from output_writers.webpage_markdown import WebpageMarkdownWriter
from output_writers.webpage_sqlite import WebpageSqlite
from scrapers.webpage_scraper import WebpageScraper

URL = "https://compartilhandobr.com/posts/red-team-operator"
URL = "https://download-cursos.netlify.app/posts/red-team-operator"


# requests = cfg.ConfigSectionReader("./configs/html_downloaders.ini", "Requests")
# html_downloader = RequestsHTMLDownloader(requests.configs)
# html_downloaded = html_downloader.get_html(URL)

# With Cache Feature
# requests = cfg.ConfigSectionReader("./configs/html_downloaders.ini", "RequestsCache")
# html_downloader = RequestsCacheHTMLDownloader(requests.configs, "webpage")
# html_downloaded = html_downloader.get_html(URL)


# html_parser = BeautifulSoupHTMLParser()
# parsed_html = html_parser.parse_html(html_downloaded)

# # person_scraper = scrapers.PersonScraper(parsed_html)
# # myperson = person_scraper.scrape()

# webpage_scraper = WebpageScraper()
# page_model = webpage_scraper.scrape(parsed_html)
# print(page_model.html)

URL = "https://download-cursos.netlify.app"
webpage_crawler = Director.construct(WebpageCrawler)
webpage_model: Webpage = webpage_crawler.crawl(URL)
writer = WebpageMarkdownWriter()
writer.save(webpage_model)
# print(webpage_model.h1_headings)

# os.remove("outputs/teste.db")
writer_configs = cfg.ConfigSectionReader("./configs/outputs.ini", "WebpageSqlite")
sqlite_writer = WebpageSqlite("teste.db", writer_configs.configs)
sqlite_writer.save(webpage_model)
print(sqlite_writer.does_this_webpage_exist(webpage_model))
