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

    links: ResultSet | list
    meta: ResultSet | list
    scripts: ResultSet | list

    json_scripts: list[dict]

    h1_headings: ResultSet | list
    h2_headings: ResultSet | list
    h3_headings: ResultSet | list
    h4_headings: ResultSet | list
    h5_headings: ResultSet | list
    h6_headings: ResultSet | list
