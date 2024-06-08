import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DemoRightClickDoubleClick:
    def demo_perform_right_click(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(2)
        actionchanins = ActionChains(driver)  # created an object of Action chain class and accept the argument driver
        #right_click_btn_element = driver.find_element(By.XPATH, '//span[@class="context-menu-one btn btn-neutral"]')
        actionchanins.context_click(driver.find_element(By.XPATH, '//span[@class="context-menu-one btn btn-neutral"]')).perform()
        time.sleep(2)
        driver.find_element(By.XPATH,'//li[@class="context-menu-item context-menu-icon context-menu-icon-copy"]').click()
        time.sleep(2)

    def demo_perform_double_click(self):
        driver = webdriver.Chrome()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(2)
        actionchanins = ActionChains(driver)
        actionchanins.double_click(driver.find_element(By.XPATH, '//button[@ondblclick="myFunction()"]')).perform()
        time.sleep(2)


findbyid = DemoRightClickDoubleClick()
findbyid.demo_perform_right_click()
findbyid.demo_perform_double_click()
