import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DemoHandleMouseHover:
    def demo_handle_mouse_hover_1(self):
            driver = webdriver.Chrome()
            driver.get("https://www.yatra.com/")
            driver.maximize_window()
            time.sleep(4)
            more_element = driver.find_element(By.XPATH, '//span[@class="more-arr"]')
            actionchains = ActionChains(driver)
            actionchains.move_to_element(more_element).perform()
            time.sleep(4)
            driver.find_element(By.XPATH, '//a[@title="Xplore"]').click()
            time.sleep(4)

    def demo_handle_mouse_hover_2(self):
            driver = webdriver.Chrome()
            driver.get("https://www.yatra.com/")
            driver.maximize_window()
            time.sleep(4)
            my_account = driver.find_element(By.XPATH, '//li[@id="userLoginBlock"]')
            actionchains = ActionChains(driver)
            actionchains.move_to_element(my_account).perform()
            time.sleep(4)
            driver.find_element(By.XPATH, '//a[@data-trackaction="Corporate Login"]').click()
            time.sleep(4)


findbyid = DemoHandleMouseHover()
findbyid.demo_handle_mouse_hover_1()
findbyid.demo_handle_mouse_hover_2()
