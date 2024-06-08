import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# driver.get("https://training.rcvacademy.com/") - 1
# driver.current_url - 2
# driver.back() - 7
# driver.forward() - 8
# driver.refresh() - 6
# driver.title - 3
# driver.maximize_window() - 4
# driver.minimize_window() - 9
# driver.fullscreen_window() -5
# driver.close() - 10
# driver.quit() - 11

class Demoseleniumlearning:
    def demo_browser_methods(self):
        driver = webdriver.Chrome()
        driver.get("https://training.rcvacademy.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(2)
        driver.close()
        driver.quit()


findbyid = Demoseleniumlearning()
findbyid.demo_browser_methods()
