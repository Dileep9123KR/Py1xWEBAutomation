# selenium
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # steps are;
    # Click on the Make Appointment button -
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

    make_apntmnt_btn = driver.find_element(By.ID,"btn-make-appointment")
    make_apntmnt_btn.click()

    print(driver.current_url)
    # Verification can be done also here
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", 'Error wrong URL'

    username = driver.find_element(By.NAME,"username") # by name attribute
    username.send_keys("John Doe")

    password = driver.find_element(By.NAME,"password") # here we can use ID also
    # here we can use "type" which is unique but we need to sue CSS_SELECTOR
    password.send_keys("ThisIsNotAPassword")

    submit_btn = driver.find_element(By.ID,"btn-login")
    submit_btn.click()

    print(driver.current_url)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment" ,'Error wrong URL'


    print(driver.title)

    time.sleep(5)
    driver.quit()
