import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


def test_vwologin_positive():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.maximize_window()
    email = driver.find_element(By.XPATH, '//input[@id="login-username"]').send_keys("mudlh2vt1h@ezztt.com")
    password = driver.find_element(By.XPATH, '//input[@id="login-password"]').send_keys("Wingify@123")
    sign_in_button = driver.find_element(By.XPATH, '//button[@id="js-login-btn"]').click()

    # Fluent Wait:
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//h1[@class="page-heading"]'), text_="Dashboard"))
       #EC.visibility_of(By.XPATH, '//h1[@class="page-heading"]')


      #Below one is not a good practice as URL loads first and elements loads later
      #EC.url_contains("Dashboard")




    heading_element = driver.find_element(By.XPATH, '//span[@data-qa="lufexuloga"]')
    assert heading_element.text == "Py2xATB"
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType)
    driver.quit()
