import os
import sqlite3

from core.director import Director
from crawlers.webpage_crawler import WebpageCrawler

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
