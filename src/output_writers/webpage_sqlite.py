from lib.sqlite_orm.sqlite_orm import DataConverter as Convert
from lib.sqlite_orm.sqlite_orm import SQLiteConnectionHandler, SqliteORM
from src.models.webpage import Webpage

WEBPAGE_TABLE = """CREATE TABLE IF NOT EXISTS [Webpage] (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL UNIQUE,
        html TEXT NOT NULL,
        title TEXT,
        head TEXT,
        body TEXT,
        links TEXT,
        meta TEXT,
        scripts TEXT,
        json_scripts TEXT,
        h1_headings TEXT,
        h2_headings TEXT,
        h3_headings TEXT,
        h4_headings TEXT,
        h5_headings TEXT,
        h6_headings TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
"""


class WebpageSqlite:
    def __init__(self, db_name: str, configs):
        self.configs = configs
        self.db_name = self.configs.get("outputDir") + db_name
        self.sqlite = SqliteORM(self.db_name)
        self._create_webpage_table(WEBPAGE_TABLE)

    def _create_webpage_table(self, table) -> None:
        self.sqlite.create_table(table)

    def save(self, webpage: Webpage) -> bool:
        self._insert_webpage(webpage)
        return True

    def does_this_webpage_exist(self, webpage) -> bool:
        conditions = bool(self.query_webpage_by_url(webpage.url))
        return conditions

    def query_webpage_by_url(self, url: str) -> tuple:
        with SQLiteConnectionHandler(self.db_name) as cursor:
            cursor.execute(f"SELECT * FROM [Webpage] WHERE [url] = '{url}'")
            return cursor.fetchone()

    def _insert_webpage(self, webpage) -> int | None:
        url = str(webpage.url)
        html = str(webpage.html)
        title = str(webpage.title)
        head = str(webpage.head)
        body = str(webpage.body)
        links = Convert.ResultSet_to_string(webpage.links)
        meta = Convert.ResultSet_to_string(webpage.meta)
        scripts = Convert.ResultSet_to_string(webpage.scripts)
        json_scripts = Convert.list_to_string(webpage.json_scripts)
        h1_headings = Convert.ResultSet_to_string(webpage.h1_headings)
        h2_headings = Convert.ResultSet_to_string(webpage.h2_headings)
        h3_headings = Convert.ResultSet_to_string(webpage.h3_headings)
        h4_headings = Convert.ResultSet_to_string(webpage.h4_headings)
        h5_headings = Convert.ResultSet_to_string(webpage.h5_headings)
        h6_headings = Convert.ResultSet_to_string(webpage.h6_headings)
        with SQLiteConnectionHandler(self.db_name) as cursor:

            cursor.execute(
                """INSERT INTO [Webpage] (
                    url,
                    html,
                    title,
                    head,
                    body,
                    links,
                    meta,
                    scripts,
                    json_scripts,
                    h1_headings,
                    h2_headings,
                    h3_headings,
                    h4_headings,
                    h5_headings,
                    h6_headings
                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    url,
                    html,
                    title,
                    head,
                    body,
                    links,
                    meta,
                    scripts,
                    json_scripts,
                    h1_headings,
                    h2_headings,
                    h3_headings,
                    h4_headings,
                    h5_headings,
                    h6_headings,
                ),
            )
            return cursor.lastrowid
