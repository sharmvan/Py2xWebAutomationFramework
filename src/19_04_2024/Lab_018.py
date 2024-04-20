# How to navigate to another URL? by using get command but there is no any navigation command in python.
# Navigation commands are very popular in JAVA.

import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By  # Imported By from common


@pytest.mark.smoke
@allure.title("Verify thet login is working in cura website")
@allure.description("TC#1 - Simple Login check on CURA katalon website.")
def test_vwologin_negative_TC():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # we can use LINK_TEXT (simple one) because uniquely we are able to find , and directly we can use it.
    make_appointment_btn = driver.find_element(By.LINK_TEXT, "Make Appointment")
    make_appointment_btn.click()

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    print(
        driver.current_url)  # After click on "make_appointment_btn.click()", I want to make sure my current url is "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Assertion Fail Message #1 - Error Matching the URLs"
    # after comma, if there is an error, it will mention my current URL is not equal to that one.

    username = driver.find_element(By.NAME, "username")
    username.send_keys("John Doe")
    password = driver.find_element(By.ID, "txt-password")
    password.send_keys("ThisIsNotAPassword")
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    # To add a screenshot with the report:
    allure.attach(driver.get_screenshot_as_png(), name="appointment-screenshot", attachment_type=AttachmentType.PNG)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Assertion Fail Message #1 - Error Matching the URLs"

    # //a[@id="btn-make-appointment"]
    # Double /, find all the a tags where id="btn-make-appointment - This will provide 1 unique element only.

    time.sleep(2)
    driver.quit()

  # //input[@id="login-username"]
