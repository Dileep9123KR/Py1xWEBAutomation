# selenium
# Project#1 Positive TestCase
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page_positive():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    print(driver.current_url)

    email_address = driver.find_element(By.ID, "login-username")  # by id attribute
    email_address.send_keys("contact+atb5x@thetestingacademy.com")

    password = driver.find_element(By.ID, "login-password")  # by ID attribute
    password.send_keys("ATBx@1234")

    submit_btn = driver.find_element(By.ID, "js-login-btn")
    submit_btn.click()

    print(driver.current_url)
    assert driver.current_url == "https://app.vwo.com/#/login", 'Error wrong URL'
    # verify_login = driver.find_element(By.XPATH, "//h1[@class='page-heading']")
    # assert "Aman" == verify_login.text

    print(driver.title)

    time.sleep(20)
    driver.quit()
