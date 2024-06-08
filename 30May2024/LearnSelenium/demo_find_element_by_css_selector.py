import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoFindElementByIdandName:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        # driver.find_element(By.XPATH, '//input[@id="login-input"]').send_keys("test@test.com")
        driver.find_element(By.CSS_SELECTOR, '#login-input').send_keys("test@test.com")
        time.sleep(2)

findbyid = DemoFindElementByIdandName()
findbyid.locate_by_id_demo()