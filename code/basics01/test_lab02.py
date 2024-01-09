# selenium
import time

from selenium import webdriver
import logging
import pytest


def test_open_login_page():
    chrome_options = webdriver.ChromeOptions()
    # By using ChromeOptions() we can do Extensions, Window size, Proxy, JS disabled
    # give some extra arguments or extensions or any arguments
    extension_path = "C:/Users/Dr.Computers/Downloads/adblocker1x.crx"
    chrome_options.add_extension(extension_path)

    chrome_options.add_argument("--start-maximized")
    LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://google.com")

    # driver.maximize_window()
    print(driver.title)

    LOGGER.info("This is Information logs")
    time.sleep(200)
