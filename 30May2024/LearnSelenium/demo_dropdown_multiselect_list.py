import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoDropDownMultiSelect:
    def demo_dropdown_multi_select(self):
        driver = webdriver.Chrome()
        driver.get("https://www.lambdatest.com/selenium-playground/select-dropdown-demo")
        driver.maximize_window()
        time.sleep(2)

        multi_drop_down = driver.find_element(By.XPATH, '//select[@id="multi-select"]')
        Multi_Drop_Down = Select(multi_drop_down)
        Multi_Drop_Down.select_by_index(0)
        time.sleep(2)
        Multi_Drop_Down.select_by_value("Florida")
        time.sleep(2)
        Multi_Drop_Down.select_by_visible_text("New Jersey")
        time.sleep(2)
        Multi_Drop_Down.select_by_index(3)
        time.sleep(2)
        Multi_Drop_Down.select_by_value("Ohio")
        time.sleep(2)
        Multi_Drop_Down.select_by_visible_text("Texas")
        time.sleep(2)

        # Multi_Drop_Down.deselect_by_index(0)
        # time.sleep(2)
        # Multi_Drop_Down.deselect_by_value("Florida")
        # time.sleep(2)
        # Multi_Drop_Down.deselect_by_visible_text("New Jersey")
        # time.sleep(2)
        # Multi_Drop_Down.deselect_by_index(3)
        # time.sleep(2)
        # Multi_Drop_Down.deselect_by_value("Ohio")
        # time.sleep(2)
        # Multi_Drop_Down.deselect_by_visible_text("Texas")
        # time.sleep(2)

        Multi_Drop_Down.deselect_all()
        time.sleep(2)


findbyid = DemoDropDownMultiSelect()
findbyid.demo_dropdown_multi_select()
