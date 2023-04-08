import pytest
from unittest.mock import Mock, MagicMock, PropertyMock
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement

import main


class TestMainWikiPage:

    def setup_method(self):
        self.page = main.MainWikiPage()

    def teardown_method(self):
        self.page.driver.quit()

    def test_is_title_matches_pass(self):
        assert self.page.is_title_matches() is True

    def test_locate_searchbar_pass(self):
        element = self.page.locate_searchbar()
        assert isinstance(element, WebElement)

    def test_search_for_selenium(self):
        result = self.page.search_for_selenium()
        assert result is True

    def test_is_title_matches_fail(self):
        type(self.page.driver).title = PropertyMock(return_value="You will not pass!")
        assert self.page.is_title_matches() is False


if __name__ == '__main__':
    pytest.main(['-d'])

