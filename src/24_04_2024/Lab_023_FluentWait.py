# "Fluent Wait" is also a type of "Explicit Wait" only.
import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)

@pytest.mark.smoke
@allure.description("TC#1 - Simple login check on vwo.com website.")
def test_vwologin_negative_TC():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    email = driver.find_element(By.XPATH, '//input[@id="login-username"]').send_keys("admin@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@id="login-password"]').send_keys("admin")
    sign_in_button = driver.find_element(By.XPATH, '//button[@id="js-login-btn"]').click()

# Fluent wait:
# I want poll after 1 sec only.
# Also, I want to ignore some type of exceptions
# We have added poll_frequency=1 so after 1 sec only, it will check.
    ignore_list=[ElementNotVisibleException,ElementNotSelectableException]

    WebDriverWait(driver=driver,timeout=5, poll_frequency=1, ignored_exceptions=ignore_list).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="js-notification-box-msg"]'))) # This is fluent wait.

# implicit wait:
# There was no concept of pole frequency. We were checking t=0, t=0.2, 0.3_________till t=5 seconds continuously checking element is visible.
# Explicit wait: (make it little better) is used with some conditions and
# Explicit wait with fluent wait is used with polling frequency.
# In this wait by using fluent wait we have mentioned that okay check for t=1,2,3,4,5
# If i keep poll_frequency=0.2 then it will check for 5/0.2=25 times

    error_msg_element = driver.find_element(By.XPATH, '//div[@id="js-notification-box-msg"]')
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    allure.attach(driver.get_screenshot_as_png(), name="Login-Screenshot", attachment_type=AttachmentType)

    driver.quit()