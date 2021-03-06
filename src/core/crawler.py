from abc import ABC, abstractmethod


class Crawler(ABC):
    @abstractmethod
    def crawl(self, url: str):
        "Return the model populated"
