"""This is the main module of the projects. Selenium script is written here."""

import pyautogui
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages import MainWikiPage, SeleniumWikiPage, GoogleChromeWikiPage, DinoGameWikiPage
from dino import Dino


if __name__ == '__main__':
    # Create a Chrome driver to connect to.
    PATH = "C:\\Program Files (x86)\\chromedriver.exe"
    service = Service(PATH)
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(3)

    # Download Wikipedia main page via driver
    page = MainWikiPage(driver)
    page.driver.get("https://www.wikipedia.org/")

    # Look for search field on the web page
    searchbar = page.locate_searchbar()
    searchbar.clear()

    # Type 'Selenium (software)' into the search field
    searchbar.send_keys("Selenium (software)")
    searchbar.send_keys(Keys.RETURN)

    try:
        selenium = SeleniumWikiPage(driver)

        # Find all chapters on the Selenium wiki page
        selenium_page_chapters = selenium.find_chapters()

        for item in selenium_page_chapters:
            print(item)

        # Find the link to Google Chrome Wiki page
        chrome = selenium.driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[16]/a[2]")
        title_ = chrome.get_attribute("title")
        print(title_)

        # Click the link
        chrome.click()

        # Move to the Google Chrome wiki page
        chrome_page = GoogleChromeWikiPage(driver)

        # Maximize the browser window
        chrome_page.driver.maximize_window()

        # Measure window's dimensions
        page_size = pyautogui.size()

        # Find the colors used on the webpage table
        chrome_page_colors = chrome_page.find_table_color()
        for color in chrome_page_colors:
            print(color)

        # Find the links to Dino Game Wiki webpage and download it
        dino_link = chrome_page.find_dinosaur_game()
        dino_game = DinoGameWikiPage(driver)

        try:
            # Move to the dino game page itself
            dino_game.driver.get("chrome://dino")

        except WebDriverException:
            # This weird exception block allows to use dino while staying connected to the internet
            pass

        # Initializes the dino bot when the chrome://dino is fully downloaded.
        # Press 'q' to leave the game
        if dino_game.wait_for_it("main-message"):
            dino_play = Dino()
            dino_play.start_game(*page_size)

    except Exception as e:
        print(f"{e.__class__}: {e}")

    finally:
        page.driver.quit()
