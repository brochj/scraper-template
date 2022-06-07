#!/home/broch/pj/scraper-template/.venv/bin/python


class LinksFormatter:
    REPLACE_THESE_WITH_EMPTY_STRING = ["#comment-area"]

    # Usado para formatar o arquivo "links.txt" que o get_links.sh vai gerar
    REMOVE_LINK_THAT_EQUALS_TO = [
        "https://compartilhandobr.com/",
        "https://downloadcursos.gratis/",
    ]

    REMOVE_LINK_THAT_CONTAINS = [
        # Compatilhandobr.com
        "/#content",
        "/404",
        "/author/admin",
        "/category/",
        "/como-baixar-arquivos-no-site/",
        "/contato/",
        "/feed/",
        "/page/",
        "/politica-de-privacidade/",
        "/regras/",
        "/reportar-dmca",
        "/termos-de-uso/",
        "author/username",
        "t.me",
        "thewpclub.com",
        "wordpress",
        # Downloadcursos.gratis
        "/politica-de-copyright/",
        "ad.a-ads.com/",
        "flaunt7.com",
        # Baixegratis.net
        "bittorrent.",
        "utorrent.",
        "bitcomet.",
        "/dmca",
        "wp-json/wp/",
        "/parceria/",
        "vuze.com",
        "pc-game-crack",
        "pc-game-",
        "web-dl-1080p",
        ".net/cd-",
        "dual-audio",
        "any-video-converter",
        "mod-apk",
        "pc-torrent",
        "/o-script/",
        "-portatil-",
        "correcao-torrent",
        "pre-ativado",
    ]

    def __init__(self) -> None:
        pass

    def replace_with(
        self, term: str, lines: list[str], new_term: str = ""
    ) -> list[str]:
        return [l.replace(term, new_term) for l in lines]

    def remove_line_that_contains(self, term: str, lines: list[str]) -> list[str]:
        return [l for l in lines if not term in l]

    def remove_line_that_equals_to(self, term: str, lines: list[str]) -> list[str]:
        return [l for l in lines if not term == l]

    def find_uniques(self, lst: list[str]) -> list[str]:
        uniques = set(lst)
        return list(uniques)

    def is_link(self, link: str) -> bool:
        return ("https://" in link) or ("http://" in link)

    def format_list(self, filename: str) -> list[str]:

        lines = read_lines(filename)

        raw_links = [l.strip() for l in lines if self.is_link(l)]
        links = self.find_uniques(raw_links)

        for link in self.REMOVE_LINK_THAT_EQUALS_TO:
            links = self.remove_line_that_equals_to(link, links)

        for term in self.REMOVE_LINK_THAT_CONTAINS:
            links = self.remove_line_that_contains(term, links)

        for term in self.REPLACE_THESE_WITH_EMPTY_STRING:
            links = self.replace_with(term, links)

        save_list_to_txt(links, filename + "-formatted")

        return links


def read_lines(filename: str):
    with open(f"{filename}.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()


def save_list_to_txt(values: list[str], filename: str) -> None:
    with open(filename + ".txt", "w", encoding="utf-8") as file:
        for value in values:
            file.write(str(value) + "\n")


if __name__ == "__main__":
    import sys

    filename = "links"
    output_filename = "formatted_links"

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        output_filename = sys.argv[2]

    links = LinksFormatter().format_list(filename)
