import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DemoHandleSliders:
    def demo_handle_sliders(self):
        driver = webdriver.Chrome()
        driver.get("https://www.snapdeal.com/products/mobiles-plain-back-covers?sort=plrty")
        driver.maximize_window()
        time.sleep(2)
        elem1 = driver.find_element(By.XPATH, '//a[contains(@class,"left-handle")]')
        elem2 = driver.find_element(By.XPATH, '//a[contains(@class,"right-handle")]')

        # 1st Way: using "drag_and_drop_by_offset()"
        # ActionChains(driver).drag_and_drop_by_offset(elem1, 50, 0).perform()

        # 2nd Way: using "click_and_hold()"
        # ActionChains(driver).click_and_hold(elem1).pause(2).move_by_offset(50,0).release().perform()

        # 3rd Way: using "move_to_element()"
        # ActionChains(driver).move_to_element(elem1).pause(2).click_and_hold(elem1).move_by_offset(50,
        #                                                                                        0).release().perform()

        # ActionChains(driver).drag_and_drop_by_offset(elem2, -50, 0).perform()

        ActionChains(driver).drag_and_drop_by_offset(elem1, 80, 0).perform()
        time.sleep(2)
        ActionChains(driver).drag_and_drop_by_offset(elem2, -50, 0).perform()
        time.sleep(2)


findbyid = DemoHandleSliders()
findbyid.demo_handle_sliders()

