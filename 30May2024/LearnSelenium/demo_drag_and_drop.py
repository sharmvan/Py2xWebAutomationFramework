import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DemoDragAndDrop:
    def demo_drag_and_drop(self):
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@class="demo-frame"]'))
        elem1 = driver.find_element(By.XPATH, '//div[@id="draggable"]')
        elem2 = driver.find_element(By.XPATH, '//div[@id="droppable"]')

        # 1st way: using drag_and_drop()
        # ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        # time.sleep(5)

        # 2nd way: using drag_and_drop_by_offset()
        ActionChains(driver).drag_and_drop_by_offset(elem1, 100, 80).perform()
        time.sleep(5)


findbyid = DemoDragAndDrop()
findbyid.demo_drag_and_drop()
