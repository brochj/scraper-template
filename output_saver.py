from abc import ABC, abstractmethod
from inspect import cleandoc

from models.model import Model
from models.webpage import Webpage


class OutputWriter(ABC):
    @abstractmethod
    def save(self, model: Model) -> bool:
        pass


class WebpageMarkdownWriter(OutputWriter):
    def save(self, model: Webpage) -> bool:
        try:
            text: str = self.format_markdown(model)
            self.save_2_md("outputs", "webpage", text)
            return True
        except FileNotFoundError as error:
            print(error)
            return False

    def format_markdown(self, model: Webpage) -> str:
        markdown = cleandoc(
            f"""
---
url: '{model.url}'
title: '{model.title.get_text()}'
links: '{[a.get_text() for a in model.links]}'
meta: '{model.meta}'
scripts: '{model.json_scripts}'
---
<h2>Descrição</h2>
{model.html}
            """
        )
        return markdown.strip()

    def save_2_md(self, foldername: str, filename: str, text: str):
        with open(f"{foldername}/{filename}.md", "w", encoding="utf-8") as file:
            file.write(text)
