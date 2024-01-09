# selenium
# Project#1 Negative TestCase
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page_negative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    print(driver.current_url)

    email_address = driver.find_element(By.ID, "login-username")  # by id attribute
    email_address.send_keys("admin")

    password = driver.find_element(By.ID, "login-password")  # by ID attribute
    password.send_keys("admin")

    submit_btn = driver.find_element(By.ID, "js-login-btn")
    submit_btn.click()

    error_msg = driver.find_element(By.CLASS_NAME,"notification-box-description").text
    assert "Your email, password, IP address or location did not match" == error_msg

    print(driver.title)

    time.sleep(20)
    driver.quit()
