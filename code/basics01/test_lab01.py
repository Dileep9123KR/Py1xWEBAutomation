# selenium

from selenium import webdriver
import logging

def test_open_login_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    LOGGER = logging.getLogger(__name__)

    driver.get("https://app.vwo.com")
    # print(driver.title)
    LOGGER.info(driver.title)