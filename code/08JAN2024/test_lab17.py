# selenium working with different web browsers at the same time
# to run these simultaneously we need to install the module named pytest-xdist
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_open_login_page_chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.title == "CURA Healthcare Service"

    mk_apntmnt_btn = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    mk_apntmnt_btn.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()


def test_open_login_page_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.title == "CURA Healthcare Service"

    mk_apntmnt_btn = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    mk_apntmnt_btn.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()

# XPATH Funtions
# Text() - //a[text()='Make Appointment'] -> Full visible Text Match
# partial => Contains() - //a[contains(text(), 'Make App')] or //a[contains(text(), 'Make')]
# Starts-with() - //a[starts-with(text(), 'Make')] -> the word starts with "Make"  will include

# XPATH OR and AND
# //p[contains(text(),'A') and contains(@class, 'mute')]
# //p[contains(text(),'A') or contains(@class, 'mute')] -> this will return a list of items
