# selenium
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.title == "CURA Healthcare Service"

    mk_apntmnt_btn = driver.find_element(By.XPATH,"//a[@id='btn-make-appointment']")
    mk_apntmnt_btn.click()

    # mk_apntmnt_btn_text = driver.find_element(By.XPATH, "//a[text()='Make Appointment']")
    # mk_apntmnt_btn_text.click()
    #
    # mk_apntmnt_btn_text_partial = driver.find_element(By.XPATH, "//a[contains(text(), 'Make App')]")
    # mk_apntmnt_btn_text_partial.click()

    pt = driver.find_element(By.CLASS_NAME, "text-muted")
    print(pt.text)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()


    # XPATH Funtions
    # Text() - //a[text()='Make Appointment'] -> Full visible Text Match
    # partial => Contains() - //a[contains(text(), 'Make App')] or //a[contains(text(), 'Make')]
    # Starts-with() - //a[starts-with(text(), 'Make')] -> the word starts with "Make"  will include