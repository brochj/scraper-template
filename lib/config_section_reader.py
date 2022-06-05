import configparser as cfg


class ConfigSectionReader:
    def __init__(self, filepath: str, section: str) -> None:

        self.parser = cfg.ConfigParser(interpolation=cfg.ExtendedInterpolation())

        self.configs: cfg.SectionProxy = self._read_section(filepath, section)

    def _read_section(self, filepath: str, section: str):
        self.parser.read(filepath)
        return self.parser[section]
