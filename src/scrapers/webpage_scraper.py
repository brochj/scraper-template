import json
from typing import Union

from bs4 import BeautifulSoup, Tag
from src.core.html_parser import HTMLParser
from src.core.scraper import Scraper
from src.exceptions.invalid_page import InvalidPage
from src.models.webpage import Webpage


class WebpageScraper(Scraper):
    def __init__(self, model: Webpage = Webpage()) -> None:
        super().__init__(model)

    def scrape(self, html: BeautifulSoup, url: str) -> Webpage:
        self.html = html
        self.model.url = url
        self.model.html = html
        # self.is_valid_page()
        self.model.title = self.get_title()
        self.model.head = self.get_head()
        self.model.body = self.get_body()
        self.model.links = self.get_links()
        self.model.meta = self.get_meta()
        self.model.scripts = self.get_scripts()
        self.model.json_scripts = self.get_json_scripts()
        self.model.h1_headings = self.get_h1_headings()
        self.model.h2_headings = self.get_h2_headings()
        self.model.h3_headings = self.get_h3_headings()
        self.model.h4_headings = self.get_h4_headings()
        self.model.h5_headings = self.get_h5_headings()
        self.model.h6_headings = self.get_h6_headings()
        return self.model

    def is_valid_page(self) -> None:
        if not self.html.select("post-item"):
            raise InvalidPage("this page does not contain a 'div.post-content'")
        if not self.html.select("post-nav"):
            raise InvalidPage("this page does not contain a 'div.post-nav'")

    def get_title(self) -> Union[Tag, str]:
        if not self.html.select("title"):
            raise InvalidPage("cannot get the post title")
        return self.safeGetOne(self.html, "title")

    def get_head(self):
        return self.safeGetOne(self.html, "head")

    def get_body(self):
        return self.safeGetOne(self.html, "body")

    def get_links(self):
        return self.safeGet(self.html, "a")

    def get_meta(self):
        return self.safeGet(self.html, "meta")

    def get_scripts(self):
        return self.safeGet(self.html, "script")

    def get_json_scripts(self) -> list[dict[str, str]]:
        scripts = self.safeGet(self.html, "script[type='application/ld+json']")
        scripts_list: list[dict[str, str]] = list()
        for script in scripts:
            scripts_list.append(json.loads(script.string))
        return scripts_list

    def get_h1_headings(self):
        return self.safeGet(self.html, "h1")

    def get_h2_headings(self):
        return self.safeGet(self.html, "h2")

    def get_h3_headings(self):
        return self.safeGet(self.html, "h3")

    def get_h4_headings(self):
        return self.safeGet(self.html, "h4")

    def get_h5_headings(self):
        return self.safeGet(self.html, "h5")

    def get_h6_headings(self):
        return self.safeGet(self.html, "h6")
