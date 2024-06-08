import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoHiddenElement:
    def demo_hidden_element_fromw3school(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        print(driver.find_element(By.XPATH, '//div[@id="myDIV"]').is_displayed())
        time.sleep(2)
        driver.find_element(By.XPATH, '//button[@class="ws-btn w3-hover-black w3-dark-grey"]').click()
        print(driver.find_element(By.XPATH, '//div[@id="myDIV"]').is_displayed())
        time.sleep(2)

    def demo_hidden_element_yatra(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/hotels")
        driver.maximize_window()
        driver.find_element(By.XPATH,'//span[@class="txt-ellipses hotel_passengerBox travellerPaxBox"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'(//span[@class="ddSpinnerPlus"])[2]').click()
        time.sleep(2)
        print(driver.find_element(By.XPATH,'//select[@class="ageselect"]').is_displayed())

        print(driver.find_element(By.XPATH,'//span[@class="ddSpinnerMinus disabled"]').click())
        time.sleep(2)
        print(driver.find_element(By.XPATH, '//select[@class="ageselect"]').is_displayed())





findbyid = DemoHiddenElement()
# findbyid.demo_hidden_element_fromw3school()
findbyid.demo_hidden_element_yatra()

