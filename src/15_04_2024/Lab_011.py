# quit command-->
from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")  # GET request to URL parameters
    print(driver.title)  # It Returns the title of the current page.
    # print(driver.page_source)
    print(driver.session_id)  # A unique id which is created when you have started a browser.
    driver.maximize_window()
    assert driver.title == "Login - VWO"  # We can add assertions also as we are using pytest
    time.sleep(10)
    driver.quit()  # 80% we use this because it deletes everything.
    # quit will close all the windows or tabs.
    # In this case, session id == null. It will become invalid.
    # It will close all other tabs.
    time.sleep(10)

# driver.quit()
