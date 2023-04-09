import pytest
from unittest.mock import Mock, MagicMock, PropertyMock
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement

import main


class TestMainWikiPage:

    def setup_method(self):
        service = Service("C:\\Program Files (x86)\\chromedriver.exe")
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(service=service, options=option)
        self.driver.implicitly_wait(3)
        self.page = main.MainWikiPage(self.driver)
        self.page.driver.get("https://www.wikipedia.org/")

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


class TestSeleniumWikiPage:

    def setup_method(self):
        service = Service("C:\\Program Files (x86)\\chromedriver.exe")
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(service=service, options=option)
        self.driver.implicitly_wait(3)
        self.page = main.SeleniumWikiPage(self.driver)
        self.page.driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")

    def teardown_method(self):
        self.page.driver.quit()

    def test_is_title_matches_pass(self):
        assert self.page.is_title_matches() is True

    def test_wait_for_it_pass(self):
        assert self.page.wait_for_it("image") is True

    def test_wait_for_it_fail(self):
        with pytest.raises(TimeoutException):
            self.page.wait_for_it("pycon")

    def test_find_chapters_pass(self):
        expecter_chapters = {"Selenium IDE", "Selenium WebDriver", "Selenium Grid",
                             "Selenium client API", "Selenium Remote Control"}
        chapters = self.page.find_chapters()
        assert chapters == expecter_chapters

    def test_find_chapters_fail(self):
        chapters = self.page.find_chapters()
        assert (chapters == {None}) is False


if __name__ == '__main__':
    pytest.main(['-d'])

