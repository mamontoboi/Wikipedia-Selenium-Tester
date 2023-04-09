import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from abc import ABC, abstractmethod
from pages import MainWikiPage, SeleniumWikiPage, GoogleChromeWikiPage


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

        chrome = selenium.driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[16]/a[2]")
        title_ = chrome.get_attribute("title")
        print(title_)

        chrome.click()
        chrome_page = GoogleChromeWikiPage(driver)
        chrome_page_colors = chrome_page.find_table_color()
        for color in chrome_page_colors:
            print(color)

        dino = chrome_page.find_dinosaur_game()

        time.sleep(5)

    except Exception as e:
        print(f"{e.__class__}: {e}")
        page.driver.quit()












