import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoToHandleCalendar:
    def demo_to_handle_calendar(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)

        driver.find_element(By.XPATH, '//input[@id="BE_flight_origin_date"]').click()
        time.sleep(4)
        # # Not recommended way:
        # driver.find_element(By.XPATH, '//td[@id="04/06/2024"]').click()
        # time.sleep(4)

        all_active_dates = driver.find_elements(By.XPATH, '//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD"]')
        for active_dates in all_active_dates:
            if active_dates.get_attribute("data-date") == "04/08/2024":
                active_dates.click()
                time.sleep(2)
                break


findbyid = DemoToHandleCalendar()
findbyid.demo_to_handle_calendar()
