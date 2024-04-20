import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_idrive360_login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    username_element = driver.find_element(By.XPATH, "//input[@id='username']")
    username_element.send_keys("augtest_040823@idrive.com")
    time.sleep(2)
    password_element = driver.find_element(By.XPATH, "//input[@id='password']")
    password_element.send_keys(123456)
    time.sleep(2)
    sign_in_button = driver.find_element(By.ID, "frm-btn")
    sign_in_button.click()
    time.sleep(50)
    allure.attach(driver.get_screenshot_as_png(),name="login_screenshot",attachment_type="upgradenow")
    print(driver.current_url)
    assert driver.current_url=="https://www.idrive360.com/enterprise/account?upgradenow=true"
    driver.quit()