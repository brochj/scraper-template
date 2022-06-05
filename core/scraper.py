from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Union

from bs4 import ResultSet, Tag
from html_parsers.beautiful_soup_html_parser import HTMLParser
from models.model import Model

T = TypeVar("T")


class Scraper(ABC):
    def __init__(self, html: HTMLParser, model: Model) -> None:
        self.html = html
        self.model = model

    def safeGet(self, pageTag, selector) -> Union[ResultSet, list]:
        childObj = pageTag.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj
        return []

    def safeGetOne(self, pageTag, selector) -> Union[Tag, str]:
        childObj = pageTag.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0]
        return ""

    @abstractmethod
    def scrape(self) -> Model:
        return self.model
