from dataclasses import dataclass
from bs4 import Tag


@dataclass
class Website(init=False):
    """Contains information about website"""

    name: str
    url: list[Tag]
    searchUrl: list[Tag]
    resultListing: list[Tag]
    resultUrl: list[Tag]
    absoluteUrl: list[Tag]
