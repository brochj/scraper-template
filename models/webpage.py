from dataclasses import dataclass
from typing import Union

from bs4 import BeautifulSoup, ResultSet, Tag

from models.model import Model


@dataclass(init=False)
class Webpage(Model):
    """Contains information about webpage structure"""

    url: str

    html: BeautifulSoup

    title: Tag
    head: Tag
    body: Tag

    links: Union[ResultSet, list]
    meta: Union[ResultSet, list]
    scripts: Union[ResultSet, list]

    json_scripts: list[dict]

    h1_headings: Union[ResultSet, list]
    h2_headings: Union[ResultSet, list]
    h3_headings: Union[ResultSet, list]
    h4_headings: Union[ResultSet, list]
    h5_headings: Union[ResultSet, list]
    h6_headings: Union[ResultSet, list]
