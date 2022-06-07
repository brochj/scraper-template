import os
import sqlite3

from src.core.director import Director
from src.crawlers.webpage_crawler import WebpageCrawler
from src.exceptions.invalid_page import InvalidPage

URLS = [
    "https://compartilhandobr.com/posts/red-team-operator",
    "https://download-cursos.netlify.app/posts/red-team-operator",
    "https://download-cursos.netlify.app",
]

webpage_crawler = Director.construct(WebpageCrawler)
for url in URLS:
    try:
        webpage_crawler.crawl(url)
    except sqlite3.IntegrityError:
        print("this url was already crawled")
    except InvalidPage as error_message:
        print(error_message)
    finally:
        print("Crawling next link...")
