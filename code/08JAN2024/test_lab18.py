# selenium
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/xpath/")

    assert driver.current_url == "https://awesomeqa.com/xpath/"

    mammal_ancestor = driver.find_element(By.XPATH,"//div[@class='Mammal']/ancestor::div")
    print(mammal_ancestor.text)

    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(5)
    driver.quit()


    # XPATH Funtions
    # Text() - //a[text()='Make Appointment'] -> Full visible Text Match
    # partial => Contains() - //a[contains(text(), 'Make App')] or //a[contains(text(), 'Make')]
    # Starts-with() - //a[starts-with(text(), 'Make')] -> the word starts with "Make"  will include

    # XPATH OR and AND
    # //p[contains(text(),'A') and contains(@class, 'mute')]
    # //p[contains(text(),'A') or contains(@class, 'mute')] -> this will return a list of items