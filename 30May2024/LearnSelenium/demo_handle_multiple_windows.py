import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoHandleMultipleWindows:
    def demo_handle_multiple_windows(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH,
                            '//div[@class="image-holder"]//img[@src="//www.yatra.com/ythomepagecms/media/todayspick_home/2024/May/8b0e72ca254455e37af5137626562b62.jpg"]').click()
        time.sleep(2)

        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, '//a[@id="booking_engine_cabs"]').click()
                time.sleep(2)
                driver.close()  # it will close child window.
                time.sleep(2)
                break
        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH,
                            '//div[@class="image-holder"]//img[@src="//www.yatra.com/ythomepagecms/media/todayspick_home/2024/May/8b0e72ca254455e37af5137626562b62.jpg"]').click()
        time.sleep(5)
        

findbyid = DemoHandleMultipleWindows()
findbyid.demo_handle_multiple_windows()
