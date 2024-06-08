import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoCheckBox:
    def demo_checkbox(self):
        driver = webdriver.Chrome()
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        driver.maximize_window()
        driver.find_element(By.XPATH, '//input[@value="red"]').click()
        time.sleep(2)
        print(driver.find_element(By.XPATH, '//input[@value="red"]').is_selected())

        # driver.find_element(By.XPATH, '//input[@value="yellow"]').click()
        # time.sleep(2)
        print(driver.find_element(By.XPATH, '//input[@value="yellow"]').is_selected())

        # driver.find_element(By.XPATH, '//input[@value="blue"]').click()
        # time.sleep(2)
        print(driver.find_element(By.XPATH, '//input[@value="blue"]').is_selected())


findbyid = DemoCheckBox()
findbyid.demo_checkbox()
