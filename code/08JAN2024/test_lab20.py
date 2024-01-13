# selenium
# CSS SELECTOR
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"
    print(driver.current_url)

    email_ip_bx = driver.find_element(By.CSS_SELECTOR,"#login-username")
    email_ip_bx.send_keys("contact+atb5x@thetestingacademy.com")
    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    #pswd_ip_bx = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    pswd_ip_bx = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    pswd_ip_bx.send_keys("ATBx@1234")

    sign_in_btn = driver.find_element(By.CSS_SELECTOR,"[id='js-login-btn']")
    sign_in_btn.click()

    print(driver.current_url)

    #assert driver.current_url == "https://app.vwo.com/#/dashboard", 'Wrong URL'

    time.sleep(15)
    driver.quit()


    # XPATH Funtions
    # Text() - //a[text()='Make Appointment'] -> Full visible Text Match
    # partial => Contains() - //a[contains(text(), 'Make App')] or //a[contains(text(), 'Make')]
    # Starts-with() - //a[starts-with(text(), 'Make')] -> the word starts with "Make"  will include

    # XPATH OR and AND
    # //p[contains(text(),'A') and contains(@class, 'mute')]
    # //p[contains(text(),'A') or contains(@class, 'mute')] -> this will return a list of items