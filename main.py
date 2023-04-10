from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages import MainWikiPage, SeleniumWikiPage, GoogleChromeWikiPage, DinoGame
from dino import Dino


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
        chrome_page.driver.maximize_window()
        page_size = chrome_page.driver.get_window_size()

        chrome_page_colors = chrome_page.find_table_color()
        for color in chrome_page_colors:
            print(color)

        dino = chrome_page.find_dinosaur_game()

        dino_game = DinoGame(driver)

        try:
            dino_game.driver.get("chrome://dino")
        except WebDriverException:
            pass

        if dino_game.wait_for_it("main-message"):
            dino_play = Dino()
            dino_play.start_game(page_size['width'], page_size['height'])

    except Exception as e:
        print(f"{e.__class__}: {e}")
        page.driver.quit()












