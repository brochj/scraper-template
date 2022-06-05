from bs4 import BeautifulSoup, Tag
from abc import ABC, abstractmethod
from typing import Any


class HTMLParser(ABC):
    """Download a HTML from an url"""

    @abstractmethod
    def parse_html(self, html: str) -> Any:
        pass


class BeautifulSoupHTMLParser(HTMLParser):
    def __init__(self) -> None:
        self.parsed_html: BeautifulSoup

    def parse_html(self, html: str) -> Any:
        self.parsed_html = BeautifulSoup(html, "html.parser")
        return self.parsed_html


if __name__ == "__main__":
    HTML = """
<!doctype html>
<html>
  <head>
    <title>This is the title of the webpage!</title>
  </head>
  <body>
    <p>This is an example paragraph. Anything in the <strong>body</strong> tag will appear on the page, just like this <strong>p</strong> tag and its contents.</p>
  </body>
</html>
"""

    html_parser = BeautifulSoupHTMLParser()
    parsed_html = html_parser.parse_html(HTML)
    parsed_html = html_parser.parse_html("<html>a</html><p></p>")
    a = parsed_html.select("html")
    print(a)
