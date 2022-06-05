import pytest
import requests
from html_downloader import Requests


def test_get_html_validSite_shouldReturnAString():
    html_downloader = Requests({"userAgent": "Mozzila/5.0"})
    html_downloaded = html_downloader.get_html("https://google.com")
    assert type(html_downloaded) is str


def test_get_html_invalidSite_raisesConnectionError():
    with pytest.raises(requests.exceptions.ConnectionError):
        html_downloader = Requests({"userAgent": "Mozzila/5.0"})
        html_downloader.get_html("https://goow123wgle.o213m")
