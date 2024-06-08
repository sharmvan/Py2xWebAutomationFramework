import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoFindElementByIdandName:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        # driver.find_element(By.LINK_TEXT, 'Yatra for Business').click()
        # driver.find_element(By.PARTIAL_LINK_TEXT, 'Yatra for').click()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Holid').click()
        time.sleep(2)


findbyid = DemoFindElementByIdandName()
findbyid.locate_by_id_demo()
