from abc import ABC, abstractmethod

from bs4 import BeautifulSoup, ResultSet, Tag
from src.core.model import Model
from src.html_parsers.beautiful_soup_html_parser import HTMLParser


class Scraper(ABC):
    def __init__(self, model: Model) -> None:
        self.model = model

    def safeGet(
        self, pageTag: Tag | BeautifulSoup, selector: str
    ) -> ResultSet[Tag] | list[str]:
        childObj: ResultSet[Tag] | None
        childObj = pageTag.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj
        return []

    def safeGetOne(self, pageTag: Tag | BeautifulSoup, selector: str) -> Tag | str:
        childObj: ResultSet[Tag] | None
        childObj = pageTag.select_one(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj
        return ""

    @abstractmethod
    def scrape(self, html: HTMLParser) -> Model:
        return self.model
