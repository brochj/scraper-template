from core.scraper import Scraper
from core.html_parser import HTMLParser
from models.person import Person


class PersonScraper(Scraper):
    def __init__(self, html: HTMLParser, person: Person = Person()) -> None:
        super().__init__(html, person)

    def scrape(self) -> Person:
        self.model.age = self.get_age()
        self.model.name = self.get_name()
        print(self.model.age)
        print(self.model.name)
        print(len(self.model.age))
        print(len(self.model.name))
        return self.model

    def get_age(self):
        return self.safeGet(self.html, "meta")

    def get_name(self):
        return self.safeGet(self.html, "div")
