import pytest
from bs4 import ResultSet, Tag
from html_parsers.beautiful_soup_html_parser import BeautifulSoupHTMLParser

from scrapers.webpage_scraper import WebpageScraper

HTML = """
<!doctype html>
<html>
  <head>
    <title>This is the title of the webpage!</title>
  </head>
  <body>
    <p>This is an example paragraph. Anything in the <strong>body</strong> 
    tag will appear on the page, just like this <strong>p</strong> tag and its contents.</p>
    <a>link 1</a>
    <a>link 2</a>
    <a>link 3</a>
  </body>
</html>
"""


@pytest.fixture(scope="module")
def webpage_scraper() -> WebpageScraper:
    html_parser = BeautifulSoupHTMLParser()
    parsed_html = html_parser.parse_html(HTML)
    return WebpageScraper(parsed_html)


@pytest.fixture(scope="module")
def webpage_scraper_invalid() -> WebpageScraper:
    html_parser = BeautifulSoupHTMLParser()
    parsed_html = html_parser.parse_html("some not-parseable html text")
    return WebpageScraper(parsed_html)


def test_get_title_titleTagExists_typeIsTag(webpage_scraper: WebpageScraper):
    titleTag: Tag = webpage_scraper.get_title()
    assert type(titleTag) == Tag


def test_get_title_titleTagDoesNotExist_returnsEmptyString(
    webpage_scraper_invalid: WebpageScraper,
):
    titleTag: Tag = webpage_scraper_invalid.get_title()
    assert type(titleTag) is str


def test_get_head_headTagExists_typeIsTag(webpage_scraper: WebpageScraper):
    headTag: Tag = webpage_scraper.get_head()
    assert type(headTag) == Tag


def test_get_head_headTagDoesNotExist_returnsEmptyString(
    webpage_scraper_invalid: WebpageScraper,
):
    headTag: Tag = webpage_scraper_invalid.get_head()
    assert type(headTag) is str


def test_get_body_bodyTagExists_typeIsTag(webpage_scraper: WebpageScraper):
    bodyTag: Tag = webpage_scraper.get_body()
    assert type(bodyTag) == Tag


def test_get_body_bodyTagDoesNotExist_returnsEmptyString(
    webpage_scraper_invalid: WebpageScraper,
):
    bodyTag: Tag = webpage_scraper_invalid.get_body()
    assert type(bodyTag) is str


def test_get_links_linkTagsExist_typeIsResultSet(webpage_scraper: WebpageScraper):
    linksTag: ResultSet = webpage_scraper.get_links()
    assert type(linksTag) == ResultSet
    assert len(linksTag) == 3


def test_get_links_linkTagsDoNotExist_returnsEmptyList(
    webpage_scraper_invalid: WebpageScraper,
):
    linksTag: Tag = webpage_scraper_invalid.get_links()
    assert type(linksTag) is list


# def test_get_meta_metaExists_returns():
#     assert

# def test_get_meta_metaTagDoesNotExist_returnsEmptyList():
#     assert

# def test_get_scripts_scriptsExists_returns():
#     assert

# def test_get_scripts_scriptsTagDoesNotExist_returnsEmptyList():
#     assert

# def test_get_json_scripts_json_scriptsExists_returns():
#     assert

# def test_get_json_scripts_json_scriptsTagDoesNotExist_returnsEmptyList():
#     assert

# def test_get_h1_headings_h1_headingsExists_returns():
#     assert

# def test_get_h1_headings_h1_headingsTagDoesNotExist_returnsEmptyList():
#     assert

# def test_get_h2_headings_h2_headingsExists_returns():
#     assert

# def test_get_h2_headings_h2_headingsTagDoesNotExist_returnsEmptyList():
#     assert

# def test_get_h3_headings_h3_headingsExists_returns():
#     assert

# def test_get_h3_headings_h3_headingsTagDoesNotExist_returnsEmptyList():
#     assert

# def test_get_h4_headings_h4_headingsExists_returns():
#     assert

# def test_get_h4_headings_h4_headingsTagDoesNotExist_returnsEmptyList():
#     assert

# def test_get_h5_headings_h5_headingsExists_returns():
#     assert

# def test_get_h5_headings_h5_headingsTagDoesNotExist_returnsEmptyList():
#     assert

# def test_get_h6_headings_h6_headingsExists_returns():
#     assert

# def test_get_h6_headings_h6_headingsTagDoesNotExist_returnsEmptyList():
#     assert
