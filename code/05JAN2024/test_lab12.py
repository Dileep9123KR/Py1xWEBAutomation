# selenium
# Project#1 Positive TestCase - Start a free trial hypertext clicking
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page_positive():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    print(driver.current_url)

    start_free_trial = driver.find_element(By.TAG_NAME,"")

    print(driver.title)

    time.sleep(20)
    driver.quit()
