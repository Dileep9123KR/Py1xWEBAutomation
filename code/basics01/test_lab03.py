# selenium
import time
import pytest

from selenium import webdriver
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    LOGGER = logging.getLogger(__name__)
    driver.get("https://google.com")

    print(driver.title)

    LOGGER.info("This is Information logs")
    time.sleep(20)

    driver.quit() # Quit the browser and close all the windows and sessionid will be null
