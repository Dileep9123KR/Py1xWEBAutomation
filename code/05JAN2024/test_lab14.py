# selenium
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")

    # Relative XPATH
    rel_xpath_email = driver.find_element(By.XPATH,"//input[@type='email']")
    rel_xpath_email.send_keys("augtest_04082023@idrive.com")

    time.sleep(5)
    driver.quit()
