from dataclasses import dataclass

from bs4 import BeautifulSoup, ResultSet, Tag
from src.core.model import Model


@dataclass(init=False)
class Webpage(Model):
    """Contains information about webpage structure"""

    url: str

    html: BeautifulSoup

    title: Tag
    head: Tag
    body: Tag

    links: ResultSet[Tag] | list[str]
    meta: ResultSet[Tag] | list[str]
    scripts: ResultSet[Tag] | list[str]

    json_scripts: list[dict[str, str]]

    h1_headings: ResultSet[Tag] | list[str]
    h2_headings: ResultSet[Tag] | list[str]
    h3_headings: ResultSet[Tag] | list[str]
    h4_headings: ResultSet[Tag] | list[str]
    h5_headings: ResultSet[Tag] | list[str]
    h6_headings: ResultSet[Tag] | list[str]
