import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoRadioButton:
    def demo_radiobutton(self):
        driver = webdriver.Chrome()
        driver.get("https://artoftesting.com/samplesiteforselenium")
        driver.maximize_window()
        time.sleep(2)
        print(driver.find_element(By.XPATH, '//input[@id="male"]').is_selected())  # False
        driver.find_element(By.XPATH, '//input[@id="male"]').click()
        time.sleep(2)
        print(driver.find_element(By.XPATH, '//input[@id="male"]').is_selected())  # True

        print(driver.find_element(By.XPATH, '//input[@id="female"]').is_selected())  # False
        driver.find_element(By.XPATH, '//input[@id="female"]').click()
        time.sleep(2)
        print(driver.find_element(By.XPATH, '//input[@id="female"]').is_selected())  # True


findbyid = DemoRadioButton()
findbyid.demo_radiobutton()
