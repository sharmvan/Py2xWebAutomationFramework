import time, allure, pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify that login is working")
@allure.description("TC#1 Simple login check on flipkart.com")
def test_flipkart_positive():
    driver = webdriver.Chrome()
    driver.get("https://flipkart.com")
    driver.maximize_window()
    search_input = driver.find_element(By.NAME, "q").send_keys("AC")
    # //*[local-name()='svg']/*[contains(text(),'Search Icon')]
    # //*[text()='Search Icon']
    # search_icon = driver.find_element(By.XPATH, "//*[local-name()='svg']/*[contains(text(),'Search Icon')]")
    # search_icon.click()  # This is very common issue where "click" doesn't work, and we have to use Actions Class.
    # Sometimes we see there are certain elements where we want to click.
    # first we have to move that element and then click on it.
    svg_list = driver.find_elements(By.XPATH, "//*[local-name()='svg']")
    svg_list[0].click()
    time.sleep(5)
