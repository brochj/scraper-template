from bs4 import BeautifulSoup, Tag
from src.html_parsers.beautiful_soup_html_parser import BeautifulSoupHTMLParser

HTML = """
<!doctype html>
<html>
  <head>
    <title>This is the title of the webpage!</title>
  </head>
  <body>
    <p>This is an example paragraph. Anything in the <strong>body</strong> 
    tag will appear on the page, just like this <strong>p</strong> tag and its contents.</p>
  </body>
</html>
"""


def test_parse_html_validHtml_ReturnsTag():
    html_parser = BeautifulSoupHTMLParser()
    parsed_html = html_parser.parse_html(HTML)
    assert type(parsed_html) is BeautifulSoup


def test_parse_html_HtmlTagExists():
    html_parser = BeautifulSoupHTMLParser()
    parsed_html = html_parser.parse_html("<html><p>Nice!</p></html><a></a>")
    tag_html = parsed_html.find("html")
    assert bool(tag_html) is True
    assert type(tag_html) is Tag
