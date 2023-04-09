from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from abc import ABC, abstractmethod


class Driver:
    def __init__(self):
        self.PATH = "C:\\Program Files (x86)\\chromedriver.exe"
        self.service = Service(self.PATH)
        self.test_driver = webdriver.Chrome(service=self.service)
        self.test_driver.implicitly_wait(3)

    @property
    def driver(self):
        return self.test_driver


class AbstractPage(ABC):
    def __init__(self, page_driver):
        self.driver = page_driver

    @abstractmethod
    def is_title_matches(self):
        pass


class MainWikiPage(AbstractPage):

    def is_title_matches(self):
        return "Wikipedia" in self.driver.title

    def locate_searchbar(self):
        return self.driver.find_element(By.ID, "searchInput")

    def search_for_selenium(self):
        page_searchbar = self.locate_searchbar()
        page_searchbar.clear()
        page_searchbar.send_keys("Selenium (software)")
        page_searchbar.send_keys(Keys.RETURN)
        return "Selenium" in self.driver.title


class SeleniumWikiPage(AbstractPage):

    def is_title_matches(self):
        return "Selenium" in self.driver.title

    def wait_for_it(self, class_name):
        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        return True

    def find_chapters(self):
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


if __name__ == '__main__':
    PATH = "C:\\Program Files (x86)\\chromedriver.exe"
    service = Service(PATH)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    page = MainWikiPage(driver)
    page.driver.get("https://www.wikipedia.org/")
    searchbar = page.locate_searchbar()
    searchbar.clear()
    searchbar.send_keys("Selenium (software)")
    searchbar.send_keys(Keys.RETURN)

    try:
        selenium = SeleniumWikiPage(driver)
        selenium_page_chapters = selenium.find_chapters()

        for item in selenium_page_chapters:
            print(item)

    except WebDriverWait as e:
        print(e)
        page.driver.quit()











