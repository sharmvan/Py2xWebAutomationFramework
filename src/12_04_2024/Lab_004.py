from selenium import webdriver
import time


def test_open_vwologin():
    driver = webdriver.Chrome()  # POST request / Create the session
    driver.get("https://app.vwo.com")  # GET request to URL parameters
    time.sleep(5)
# driver.get("https://app.vwo.com") --> If I don't type any command, the moment we call "webdriver.Edge()", A
# new session will be created. only browser will get open and nothing will happen.


# driver = webdriver.Chrome()
# Note: driver is a reference. chrome is a class. we have created the reference of the class.Selenium is a parent.
# webdriver we are importing and webdriver is calling all the classes (like chrome, edge).
