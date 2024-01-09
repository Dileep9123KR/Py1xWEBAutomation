# selenium
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_btn = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_btn.click()

    # make_apntmt_btn = driver.find_element(By.PARTIAL_LINK_TEXT,"Appointment")
    # # here we can use either "Make" or "Appointment" or "Make Appointment" texts
    # make_apntmt_btn.click()

    # make_apntmt_btn = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # make_apntmt_btn.click()

    # make_apntmt_btn = driver.find_element(By.CLASS_NAME, "btn.btn-dark.btn-lg")
    # make_apntmt_btn[1].click()

    # steps are;
    # Click on the Make Appointment button -
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>
    print(driver.title)

    time.sleep(5)
    driver.quit()
