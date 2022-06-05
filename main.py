# Just for testing
import lib.config_section_reader as cfg
from html_downloaders.requests_html_downloader import Requests
from html_parsers.beautiful_soup_html_parser import BeautifulSoupHTMLParser
import scrapers

requests = cfg.ConfigSectionReader("./configs/html_downloaders.ini", "Requests")
html_downloader = Requests(requests.configs)
html_downloaded = html_downloader.get_html(
    # "https://download-cursos.netlify.app/posts/red-team-operator"
    "https://compartilhandobr.com/posts/red-team-operator"
)
html_parser = BeautifulSoupHTMLParser()
parsed_html = html_parser.parse_html(html_downloaded)

# person_scraper = scrapers.PersonScraper(parsed_html)
# myperson = person_scraper.scrape()

webpage_scraper = scrapers.WebpageScraper(parsed_html)
myperson = webpage_scraper.scrape()
# print(myperson)
