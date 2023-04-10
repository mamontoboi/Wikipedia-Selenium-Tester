"""This module contains classes, representing separate web pages on the Wikipedia."""

import re
from abc import ABC, abstractmethod
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AbstractPage(ABC):
    """Abstract class to be used as a template."""

    def __init__(self, page_driver):
        self.driver = page_driver

    @abstractmethod
    def is_title_matches(self):
        """Method to be re-defined in each child class."""


class MainWikiPage(AbstractPage):
    """Automation methods for handling of the Wikipedia main page."""

    def is_title_matches(self):
        return "Wikipedia" in self.driver.title

    def locate_searchbar(self):
        """Looks for search bar on the main Wikipedia page."""

        return self.driver.find_element(By.ID, "searchInput")

    def search_for_selenium(self):
        """Inputs `Selenium (software)` into the search bar."""

        page_searchbar = self.locate_searchbar()
        page_searchbar.clear()
        page_searchbar.send_keys("Selenium (software)")
        page_searchbar.send_keys(Keys.RETURN)
        return "Selenium" in self.driver.title


class SeleniumWikiPage(AbstractPage):
    """Automation methods for handling of the Selenium software Wiki page."""

    def is_title_matches(self):
        return "Selenium" in self.driver.title

    def wait_for_it(self, class_name):
        """Ensures that the Selenium page is loaded."""

        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        return True

    def find_chapters(self):
        """Collects all chapters from Selenium web page."""

        if self.wait_for_it("image"):
            elements = self.driver.find_elements(By.TAG_NAME, "h3")
            cleared_elements = set()
            for element in elements:
                element_text = element.text
                if element_text.endswith('[edit]'):
                    cleared_elements.add(element_text[:-6])
                else:
                    cleared_elements.add(element_text)

            return cleared_elements
        return False


class GoogleChromeWikiPage(AbstractPage):
    """Automation methods for handling of the Google Chrome Wiki page."""

    def is_title_matches(self):
        return "Google Chrome" in self.driver.title

    def wait_for_it(self, class_name):
        """Ensures that the Google Chrome Wiki web page is loaded."""

        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, class_name))
        )
        return True

    def find_table_color(self):
        """Collects color specifications from cells, containing 'yes' or 'no' in table of the Google Chrome Page."""

        if self.wait_for_it("image"):
            table_yes = self.driver.find_element(By.CLASS_NAME, "table-yes")
            green_color = table_yes.value_of_css_property('background')
            green_color = re.findall(r'rgb\(\d{3}, \d{3}, \d{3}\)', green_color)[0]

            table_no = self.driver.find_element(By.CLASS_NAME, "table-no")
            red_color = table_no.value_of_css_property('background')
            red_color = re.findall(r'rgb\(\d{3}, \d{3}, \d{3}\)', red_color)[0]

            return green_color, red_color

    def find_dinosaur_game(self):
        """Looks for the link to the Dinosaur Game Wiki page."""

        if self.wait_for_it("image"):
            dino = self.driver.find_element(By.LINK_TEXT, "Dinosaur Game")
            dino.click()
        return True


class DinoGameWikiPage(AbstractPage):
    """Automation methods for handling of the Dinosaur Game Wiki page."""

    def is_title_matches(self):
        return "Dinosaur Game" in self.driver.title

    def wait_for_it(self, id_):
        """Ensures that the Dinosaur Game Wiki web page is loaded."""
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.element_to_be_clickable((By.ID, id_))
        )
        return True
