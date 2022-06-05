import pytest
from lib.config_section_reader import ConfigSectionReader


import os
import tempfile
import shutil

CONFIG_FILE = """
[Common]
userAgent=Mozilla/5.0
server: localhost:3000
"""


@pytest.fixture(scope="module")
def config_file():
    tmpdir = tempfile.mkdtemp()
    subdir = os.path.join(tmpdir, "sub")
    os.mkdir(subdir)
    filename = os.path.join(subdir, "config.cfg")

    with open(filename, "w") as file:
        file.write(CONFIG_FILE)

    yield filename
    shutil.rmtree(tmpdir)


def test_ConfigSectionReader_ShouldReadSection(config_file):
    parser = ConfigSectionReader(config_file, "Common")
    assert parser.configs["userAgent"] == "Mozilla/5.0"
    assert parser.configs["server"] == "localhost:3000"


def test_WrongSectionName_raisesKeyError(config_file):
    with pytest.raises(KeyError):
        parser = ConfigSectionReader(config_file, "WrongSection")


# @pytest.mark.parametrize("element, expected", [('snow', 'water'), ('tin', 'solder')])
# def test_action_with_parametrization(element, expected):
#     sc = ConfigSectionReader()
#     sc.element = element
#     sc.melt()
#     assert sc.element == expected
