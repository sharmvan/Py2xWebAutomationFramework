import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoWebElementState:
    def demo_web_element_state(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        # print(driver.find_element(By.XPATH, '//input[@id="login_button"]').is_enabled())
        driver.find_element(By.XPATH, '//input[@id="user_name"]').send_keys('abc@gmail.com')
        driver.find_element(By.XPATH, '//input[@id="user_pass"]').send_keys('12345')
        print(driver.find_element(By.XPATH, '//input[@id="login_button"]').is_enabled())

        time.sleep(2)


findbyid = DemoWebElementState()
findbyid.demo_web_element_state()

