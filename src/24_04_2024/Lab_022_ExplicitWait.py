import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.smoke
@allure.description("TC#1 - Simple login check on vwo.com website.")
def test_vwologin_negative_TC():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    email = driver.find_element(By.XPATH, '//input[@id="login-username"]').send_keys("admin@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@id="login-password"]').send_keys("admin")
    sign_in_button = driver.find_element(By.XPATH, '//button[@id="js-login-btn"]').click()


# here we need to fix because now there is one problem error i.e.,
# error_msg_element will come after 5 seconds. should I tell webdriver to wait for each element(email,password,sign_in_button) for this one element?
# Ans is No.
# for this element "error_msg_element", I have to wait with some condition. Previously we have done implicit wait,
# there was no condition.Everyone have to wait.
# But for explicit wait, we can tell webdriver to wait for only particular element with condition.
# Add a condition so that webdriver should wait for that condition.
# For eg: until my page title = vwo.com, I will not move forward until error message is visible.
# We can add such kind of scenarios until this error message is seen on the DOM or HTML page - I will not read the text
# These kind of conditions I can add.

# To add a condition, we need to import 2 things (expected_conditions & WebDriverWait) mentioned at the above.
# add "WebDriverWait" , we are telling driver to wait for max 5 seconds until EC (Expected Condition) true

    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="js-notification-box-msg"]'))) # This is explicit wait.
    error_msg_element = driver.find_element(By.XPATH, '//div[@id="js-notification-box-msg"]')
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    allure.attach(driver.get_screenshot_as_png(), name="Login-Screenshot", attachment_type=AttachmentType)

    driver.quit()
# If element is available at timeout=1, then it will take only 1 sec and will proceed to next command because condition is fulfilled.
# But there is one condition, lets understand with the help of a diagram:
# we have t=0, t=1 and t=5 (This 5 sec , we have given max duration)
# Scenario 1: if element found at t=1, we saved 4 seconds.
# Scenario 2: if element found at t=5, we saved 0 seconds.
# Scenario 3: if element found at t=7, then Exception will occur.
# But there is one thing which we have problem that it is continuously checking for visibility of an element from t=0 to t=5 for
# 2nd scenario, but we can improve this by using "fluent wait". we can say webdriver like check after every one second till t=5.
# Yes it is possible if I can give frequency check after sometime.

