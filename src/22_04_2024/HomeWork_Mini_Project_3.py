import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.Username
@allure.title("Verify the error message comes when you click on the submit button")
@allure.description("TC#1 - Verify te username on cdpn.io website.")
def test_cdpn_io():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(2)

    driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='result']"))

    email=driver.find_element(By.XPATH, "//input[@id='email']").send_keys('admin@abc.com')
    time.sleep(2)
    password=driver.find_element(By.XPATH, "//input[@id='password']").send_keys("admin123")
    time.sleep(2)
    confirm_password=driver.find_element(By.XPATH, "//input[@id='password2']").send_keys("admin123")
    time.sleep(2)
    submit_btn=driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
    time.sleep(2)

    allure.attach(driver.get_screenshot_as_png(), name="Error message", attachment_type=AttachmentType.PNG)
    driver.quit()

