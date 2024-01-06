# selenium
import time

from selenium import webdriver


def test_open_login_page():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get("https://google.com")
    print(driver.title)

    time.sleep(5)
    driver.quit()

    # time.sleep(50) # time in seconds only

    # After we're done with our test cases,
    # Interview Question
    # driver.close() - close the current window(current tab), it will not close other tabs
    # driver.quit() - close all the tabs(windows) in the web browser

    # Session == None in this case
