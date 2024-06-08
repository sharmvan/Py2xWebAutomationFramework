import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoGetAttributeValue:
    def demo_get_attribute_value(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        # print(driver.find_element(By.XPATH, '//span[contains(text(),"Mauritius Holiday Packages")]').text)
        # print(driver.find_element(By.XPATH, '//input[@value="Search Flights"]').get_attribute("value"))
        print(driver.find_element(By.XPATH, '//a[@data-trackaction="Yatra For Business"]').get_attribute('data-trackaction'))
        time.sleep(2)


findbyid = DemoGetAttributeValue()
findbyid.demo_get_attribute_value()

