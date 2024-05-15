# Exception: is something which will interrupt your program. We can handle it by using try
# and accept.

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *


def test_exception_1():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    text_area = driver.find_element(By.NAME, "q")
    # Now suppose I found the element
    # And after finding the element, I refresh the window.
    # Now I will do send keys.
    driver.refresh()
    text_area.send_keys("The Testing Academy")
    time.sleep(1)
    driver.quit()


# Note: you have found the element
#       you refresh the element
# There will be 2 cases:
# 1. WebDriver will say that there can be a case where this element you have found the first element.
# It says there is a problem which is "stale element reference" exception. stale means which isn't fresh.
# Webdriver telling you I have found the element (text_area).
# But after the refresh all the DOM elements are refreshed. when you do refresh, all the documents elements
# are refreshed.
# Now webdriver is confused that probably
# [text_area = driver.find_element(By.NAME, "q")]-- this is not working. That's why it's giving you
# stale element exception.
# What refresh can perform?
# Navigate to other page, change in DOM elements. Whenever these events occur and webdriver will always get confused.
# and it will give you "stale element reference" exception


# How to handle "stale element reference" exception?
def test_exception_2():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    try:
        text_area = driver.find_element(By.NAME, "q")
        driver.refresh()
        text_area.send_keys("The Testing Academy")
    except StaleElementReferenceException as sere:
        print(sere)

    time.sleep(1)
    driver.quit()


# Note: with the above mechanism, code will not work. To fix this, after refresh we need to find the element again in the
# below test case

def test_exception_3():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    try:
        text_area = driver.find_element(By.NAME, "q")
        driver.refresh()
        # driver.switch_to.alert
        text_area = driver.find_element(By.NAME, "q")
        text_area.send_keys("The Testing Academy")
        # NoAlertPresentException
    except StaleElementReferenceException as sere:
        print(sere)

    time.sleep(1)
    driver.quit()

# If we do "driver.switch_to.alert", it will give you "NoAlertPresentException".
# Note: whenever a refresh happen, whenever you navigate a different page, whenever you using a
# framework, there can be a case where ID changes, Class changes. That's why it gives you the
# "stale element reference" exception.

