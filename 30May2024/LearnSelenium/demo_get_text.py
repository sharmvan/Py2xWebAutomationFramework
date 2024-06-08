import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoGetText:
    def demo_get_text(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/offer/dom/listing/domestic-hotel-deals")
        driver.maximize_window()
        # print(driver.find_element(By.XPATH, '//span[contains(text(),"Mauritius Holiday Packages")]').text)
        print(driver.find_element(By.XPATH, '//span[contains(text(),"Yatra Easy EMI Offer with")]').text)
        time.sleep(2)


findbyid = DemoGetText()
findbyid.demo_get_text()

