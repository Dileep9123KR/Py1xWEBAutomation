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


