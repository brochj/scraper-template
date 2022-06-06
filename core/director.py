from core.crawler_builder import CrawlerBuilder


class Director:
    "The BOSS"

    @staticmethod
    def construct(crawler_builder: CrawlerBuilder) -> None:
        return (
            crawler_builder()
            .build_configurations()
            .build_html_downloader()
            .build_html_parser()
            .get_result()
        )
