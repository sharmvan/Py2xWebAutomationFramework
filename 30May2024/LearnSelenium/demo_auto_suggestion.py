import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoAutoSuggestion:
    def demo_auto_suggestion_1(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        # depart_from = driver.find_element(By.XPATH, '//input[@id="BE_flight_origin_city"]')
        # depart_from.click()
        # time.sleep(2)
        # depart_from.send_keys("New Delhi")
        # time.sleep(2)
        # depart_from.send_keys(Keys.ENTER)
        # time.sleep(2)

        going_to = driver.find_element(By.XPATH, '//input[@id="BE_flight_arrival_city"]')
        going_to.click()
        time.sleep(4)
        going_to.send_keys("New")
        time.sleep(4)
        going_to = driver.find_elements(By.XPATH, '//div[@class="viewport"]//div[1]/li')
        print(len(going_to))
        for gt in going_to:
            print(gt.text)
            if "New Orleans (MSY)" in gt.text:
                gt.click()
                time.sleep(4)
                break


findbyid = DemoAutoSuggestion()
findbyid.demo_auto_suggestion_1()
