# selenium
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


def test_open_login_page():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.implicitly_wait(20)
    search_bx = driver.find_element(By.XPATH,"//input[@name='_nkw']")
    search_bx.click()
    search_bx.send_keys("16 gb")
    print(driver.current_url)
    search_btn = driver.find_element(By.ID,"gh-btn")
    search_btn.click()

    assert driver.current_url == "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=16+gb&_sacat=0", "Error Wrong URL"

    lists_items = driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in lists_items:
        print(i.text)

    print(driver.current_url)


    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(15)
    driver.quit()


    # XPATH Funtions
    # Text() - //a[text()='Make Appointment'] -> Full visible Text Match
    # partial => Contains() - //a[contains(text(), 'Make App')] or //a[contains(text(), 'Make')]
    # Starts-with() - //a[starts-with(text(), 'Make')] -> the word starts with "Make"  will include

    # XPATH OR and AND
    # //p[contains(text(),'A') and contains(@class, 'mute')]
    # //p[contains(text(),'A') or contains(@class, 'mute')] -> this will return a list of items