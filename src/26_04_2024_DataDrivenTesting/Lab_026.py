import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


@pytest.mark.smoke
@allure.title("Verify that login is working in 'app.vwo.com' website")
@allure.description("TC#1 - Simple login check on 'app.vwo.com' website")
def test_vwologin_positive():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # Login Scenario - We can run our login scenario multiple times with Excel File data. This is called as
    # Data Driven Testing


    driver.maximize_window()

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType)
    driver.quit()
