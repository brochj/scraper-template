import sqlite3

from src.core.director import Director
from src.crawler_builders.webpage_crawler_builder import WebpageCrawlerBuilder
from src.exceptions.invalid_page import InvalidPage

URLS = [
    "https://compartilhandobr.com/posts/red-team-operator",
    "https://download-cursos.netlify.app/posts/red-team-operator",
    "https://download-cursos.netlify.app",
    "https://google.com.br",
]

webpage_crawler = Director.construct(WebpageCrawlerBuilder())
for url in URLS:
    try:
        webpage_crawler.crawl(url)
    except sqlite3.IntegrityError:
        print("This url already exists in the database")
    except InvalidPage as error_message:
        print(error_message)
    finally:
        print("Crawling next link...")
