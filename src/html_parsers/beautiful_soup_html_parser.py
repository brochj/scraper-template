from typing import Any

from bs4 import BeautifulSoup
from src.core.html_parser import HTMLParser


class BeautifulSoupHTMLParser(HTMLParser):
    def __init__(self) -> None:
        self.parsed_html: BeautifulSoup

    def parse_html(self, html: str) -> Any:
        self.parsed_html = BeautifulSoup(html, "html.parser")
        return self.parsed_html


if __name__ == "__main__":
    # Just for testing
    HTML = """
        <!doctype html>
        <html>
            <head>
                <title>This is the title of the webpage!</title>
            </head>
            <body>
                <p>
                    This is an example paragraph. Anything in the <strong>body</strong> tag will appear on the page.
                </p>
            </body>
        </html>
        """

    html_parser = BeautifulSoupHTMLParser()
    parsed_html = html_parser.parse_html(HTML)
    parsed_html = html_parser.parse_html("<html>a</html><p></p>")
    a = parsed_html.select("html")
    print(a)
