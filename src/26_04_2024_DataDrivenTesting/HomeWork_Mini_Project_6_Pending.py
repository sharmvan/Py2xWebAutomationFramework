# Login with the Credential - https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# Add user https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser
# Search User

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
    # <<<<<<<<<<< Load website and login phase >>>>>>>>
    # Open the orange hrm website
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(2)

    # Enter credentials and click login
    username=driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
    time.sleep(2)
    password=driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
    time.sleep(2)
    login_btn=driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    # <<<<<<<<<<< Load Admin page and add user profile phase >>>>>>>>
    # Click Admin link on dashboard page
    admin_element_icon = driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
    time.sleep(2)

    # click add button to open add new profile page
    admin_add_btn = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
    time.sleep(2)

    # Enter user role, employee name, status, username and passwords. click on save.
    user_role=driver.find_elements(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']")











