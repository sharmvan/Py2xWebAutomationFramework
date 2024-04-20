# How to navigate to another URL? by using get command but there is no any navigation command in python.
# Navigation commands are very popular in JAVA.
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By  # Imported By from common


@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # Now We should interact with the "HTML elements" & "Locators".
    # Find the element the anchor tag - button
    # Click on it

    # by using: id, className, name, tagName, linkText and PartialLinkText (easy way)
    # by using: XPATH, CSS Selector (Sure shot way to find the element in HTML)
    element = driver.find_element(By.ID, "btn-make-appointment")  # It will return your web element.
    # find_element is a function which will find only one element.
    # find_elements is also a function which will find all the elements which have id="btn-make-appointment" and it
    # will return list of elements.
    element.click()  # This web element have a function which is click.
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    # time.sleep(10)
    driver.quit()
