from selenium import webdriver  # Selenium is a framework. it's basically a library that we have downloaded and
# in the selenium we have webdriver. that's why we returned from selenium import webdriver. In the webdriver, we have chrome.
import time
import pytest


@pytest.mark.smoke
def test_open_vwologin():
    # all below are nothing but API requests except assert
    driver = webdriver.Chrome()  # POST request / Create the session
    # The moment we write the line no:10, session is created with unique id which is 16-digit id.
    # Id will be like this 56dfd7fwekfewj12 (16-digits)
    # session means that a fresh copy of the browser will be created.
    # The moment you type this command: "webdriver.Chrome()", a fresh copy of browser is created.
    # In that browser, we can open new tabs, open url, those will be different from the normal browser.
    # refer lab_009 for this to see the results.

    driver.get("https://app.vwo.com")  # GET request to URL parameters
    print(driver.title)  # It Returns the title of the current page.
    # print(driver.page_source)
    print(driver.session_id)  # A unique id which is created when you have started a browser.
    driver.maximize_window()
    assert driver.title == "Login - VWO"  # We can add assertions also as we are using pytest
