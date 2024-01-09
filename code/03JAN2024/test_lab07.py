# selenium
import time
import pytest

from selenium import webdriver
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    #LOGGER = logging.getLogger(__name__)

    driver.get("https://app.vwo.com")
    print(driver.title)

    # LOGGER.info("This is Information logs")
    # LOGGER.warning("This is warning logs")
    # LOGGER.error("This is Error Logs")
    # LOGGER.critical("This is Critical logs")

    time.sleep(5)
    driver.quit()
