import os
import allure
import openpyxl
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


# Data Driven Test case for the Login Page.
# We will test invalid logins for the vwo login page.

# To make data driven, we need to prepare data in Excel.
# Which library we have used for our Excel automation in python? --> Openpyxl

def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({
            "username": username,
            "password": password
        })
    return credentials


file_path_fromos = os.getcwd() + "/testdata_ddt_123.xlsx"
print(file_path_fromos)


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(file_path_fromos))
@allure.title("Verify invalid login with the Excel Testdata")
@allure.description("TC#1 - Invalid login verification for 'app.vwo.com' website")
def test_vwologin(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    # vwologin(username=username,password=password)
    print(username, password)


def vwologin(username, password):
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()

    # Instead of hardcoding, I can set the parameters as "username","password" so that I can run
    # it multiple times.
    email = driver.find_element(By.XPATH, '//input[@id="login-username"]').send_keys(username)
    password = driver.find_element(By.XPATH, '//input[@id="login-password"]').send_keys(password)
    sign_in_button = driver.find_element(By.XPATH, '//button[@id="js-login-btn"]').click()

    # Here I can add logic:
    # Whatever the current url that we have after entering the correct username and password
    # If username and password is correct, I can see dashboard page.
    # If username and password is not correct, then I will an error message.
    result = driver.current_url
    if result != "https://app.vwo.com/#dashboard":
        ignore_list = [ElementNotVisibleException, ElementNotSelectableException]

        WebDriverWait(driver=driver, timeout=5, poll_frequency=1, ignored_exceptions=ignore_list).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@id="js-notification-box-msg"]')))

        error_msg_element = driver.find_element(By.XPATH, '//div[@id="js-notification-box-msg"]')
        print(error_msg_element.text)
        assert error_msg_element.text == "Your email, password, IP address or location did not match"
    else:
        ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
        WebDriverWait(driver=driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list).until(
            EC.text_to_be_present_in_element((By.XPATH, '//h1[@class="page-heading"]'), text_="Dashboard"))

        heading_element = driver.find_element(By.XPATH, '//span[@data-qa="lufexuloga"]')
        assert heading_element.text == "Py2xATB"

        allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType)
        driver.quit()

