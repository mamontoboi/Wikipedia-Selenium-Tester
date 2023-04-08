from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self):
        self.PATH = "C:\\Program Files (x86)\\chromedriver.exe"
        self.service = Service(self.PATH)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(3)


class MainWikiPage(BasePage):

    def __init__(self):
        super().__init__()
        self.driver.get("https://www.wikipedia.org/")

    def is_title_matches(self):
        return "Wikipedia" in self.driver.title

    def locate_searchbar(self):
        return self.driver.find_element(By.ID, "searchInput")

    def search_for_selenium(self):
        searchbar = self.locate_searchbar()
        searchbar.clear()
        searchbar.send_keys("Selenium (software)")
        searchbar.send_keys(Keys.RETURN)
        return "Selenium" in self.driver.title


if __name__ == '__main__':
    page = MainWikiPage()
    print(page.is_title_matches())
    print(page.search_for_selenium())









