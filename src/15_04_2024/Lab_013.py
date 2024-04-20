# How to navigate to another URL? by using get command but there is no any navigation command in python.
# Navigation commands are very popular in JAVA.
from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    # In Python, Navigation commands are not present.
    driver.back()
    time.sleep(5)
    driver.get("https://www.bing.com")
    print(driver.title)

    time.sleep(5)
    driver.forward()
    print(driver.title)

    time.sleep(5)
    driver.back()
    print(driver.title)
    driver.refresh()

    time.sleep(5)
    driver.quit()