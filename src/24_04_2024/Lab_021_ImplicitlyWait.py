import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType


@pytest.mark.smoke
@allure.description("TC#1 - Simple login check on vwo.com website.")
def test_vwologin_negative_TC():
    driver = webdriver.Chrome()
    #driver.implicitly_wait(5) - webdriver to wait for all the elements.
    #time.sleep(5) - In this case, Python Interpreter to wait.
    driver.get("https://app.vwo.com")

    #e1,e2,e3->
    #tell webdriver to wait for the 5 seconds to load for all the elements.
    #what if e1,e2,e3 < 3 seconds, then 2 seconds will be wasted.
    
    email = driver.find_element(By.XPATH, '//input[@id="login-username"]').send_keys("admin@gmail.com")
    password = driver.find_element(By.XPATH, '//input[@id="login-password"]').send_keys("admin")
    sign_in_button = driver.find_element(By.XPATH, '//button[@id="js-login-btn"]').click()


    time.sleep(5)
    error_msg_element = driver.find_element(By.XPATH, '//div[@id="js-notification-box-msg"]')
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    allure.attach(driver.get_screenshot_as_png(), name="Login-Screenshot", attachment_type=AttachmentType)

    driver.quit()
