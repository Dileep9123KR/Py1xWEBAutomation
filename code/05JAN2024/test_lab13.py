# selenium
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    # Absolute XPATH
    abs_xpath_email = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/div[3]/form[1]/ul/li[1]/div/input")
    abs_xpath_email.send_keys("Admin")

    time.sleep(5)
    driver.quit()
