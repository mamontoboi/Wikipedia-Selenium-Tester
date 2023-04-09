import pytest
from unittest.mock import Mock, MagicMock, PropertyMock
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement

import pages


class TestTemplate:

    def setup_method(self):
        service = Service("C:\\Program Files (x86)\\chromedriver.exe")
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(service=service, options=option)
        self.driver.implicitly_wait(3)


class TestMainWikiPage(TestTemplate):

    def setup_method(self):
        super().setup_method()
        self.page = pages.MainWikiPage(self.driver)
        self.page.driver.get("https://www.wikipedia.org/")

    def teardown_method(self):
        self.page.driver.quit()

    def test_is_title_matches_pass(self):
        assert self.page.is_title_matches() is True

    def test_is_title_matches_fail(self):
        mock_driver = Mock()
        mock_driver.title = "Not matching title"
        mock_driver.__contains__ = lambda item: item in mock_driver.title
        mock_page = pages.MainWikiPage(mock_driver)
        assert mock_page.is_title_matches() is False

    def test_locate_searchbar_pass(self):
        element = self.page.locate_searchbar()
        assert isinstance(element, WebElement)

    def test_search_for_selenium(self):
        result = self.page.search_for_selenium()
        assert result is True

    # def test_is_title_matches_fail(self):
    #     type(self.page.driver).title = PropertyMock(return_value="You will not pass!")
    #     assert self.page.is_title_matches() is False


class TestSeleniumWikiPage(TestTemplate):

    def setup_method(self):
        super().setup_method()
        self.page = pages.SeleniumWikiPage(self.driver)
        self.page.driver.get("https://en.wikipedia.org/wiki/Selenium_(software)")

    def teardown_method(self):
        self.page.driver.quit()

    def test_is_title_matches_pass(self):
        assert self.page.is_title_matches() is True

    def test_is_title_matches_fail(self):
        mock_driver = Mock()
        mock_driver.title = "Not matching title"
        mock_driver.__contains__ = lambda item: item in mock_driver.title
        mock_page = pages.SeleniumWikiPage(mock_driver)
        assert mock_page.is_title_matches() is False

    def test_wait_for_it_pass(self):
        assert self.page.wait_for_it("image") is True

    def test_wait_for_it_fail(self):
        with pytest.raises(TimeoutException):
            self.page.wait_for_it("You_will_not_find")

    def test_find_chapters_pass(self):
        expecter_chapters = {"Selenium IDE", "Selenium WebDriver", "Selenium Grid",
                             "Selenium client API", "Selenium Remote Control"}
        chapters = self.page.find_chapters()
        assert chapters == expecter_chapters

    def test_find_chapters_fail(self):
        chapters = self.page.find_chapters()
        assert (chapters is None) is False


class TestGoogleChromeWikiPage(TestTemplate):

    def setup_method(self):
        super().setup_method()
        self.page = pages.GoogleChromeWikiPage(self.driver)
        self.page.driver.get("https://en.wikipedia.org/wiki/Google_Chrome")

    def teardown_method(self):
        self.page.driver.quit()

    def test_is_title_matches_pass(self):
        assert self.page.is_title_matches() is True

    def test_wait_for_it_pass(self):
        assert self.page.wait_for_it("image") is True

    def test_wait_for_it_fail(self):
        with pytest.raises(TimeoutException):
            self.page.wait_for_it("You_will_not_find")

    def test_find_table_color(self):
        green, red = self.page.find_table_color()
        assert green == 'rgb(158, 255, 158)'
        assert red == 'rgb(255, 199, 199)'

    def test_find_dinosaur_game(self):
        self.page.find_dinosaur_game()
        assert "Dinosaur Game" in self.driver.title


if __name__ == '__main__':
    pytest.main(['-d'])

