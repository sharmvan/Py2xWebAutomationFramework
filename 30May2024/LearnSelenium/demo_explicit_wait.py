import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DemoExplicitWait:
    def demo_to_explicit_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        wait = WebDriverWait(driver, 5)
        driver.maximize_window()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="BE_flight_origin_date"]'))).click()

        all_active_dates = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD"]')))\
            .find_elements(By.XPATH, '//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD"]')

        for active_dates in all_active_dates:
            if active_dates.get_attribute("data-date") == "04/08/2024":
                time.sleep(5)
                active_dates.click()
                time.sleep(5)
                break


findbyid = DemoExplicitWait()
findbyid.demo_to_explicit_wait()
