import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.sanity
@allure.title("Login to Orange HRM page")
@allure.description("TC#1 - Verify after Adding a new user, It's getting displayed")
def test_Orange_HRM():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(1)

    username=driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
    time.sleep(1)
    password=driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    time.sleep(1)
    login_btn=driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    admin_element_icon=driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
    time.sleep(1)
