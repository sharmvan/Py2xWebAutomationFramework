import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoFindElementByIdandName:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # print(len(driver.find_elements(By.TAG_NAME, 'a')))
        anchor_tags = driver.find_elements(By.TAG_NAME, 'a')
        print(len(anchor_tags))
        for a in anchor_tags:
            print(a.text)
        # time.sleep(2)
        # print(len(driver.find_elements(By.TAG_NAME, 'input')))

findbyid = DemoFindElementByIdandName()
findbyid.locate_by_id_demo()
