import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoDropDownSingleSelect:
    def demo_dropdown_single_select(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.maximize_window()
        time.sleep(2)

        drop_down = driver.find_element(By.XPATH, '//select[@name="UserTitle"]')
        Drop_Down = Select(drop_down)

        Drop_Down.select_by_index(1)
        time.sleep(2)

        Drop_Down.select_by_value("Marketing_PR_Manager_ANZ")
        time.sleep(2)

        Drop_Down.select_by_visible_text("Customer Service Manager")
        time.sleep(2)


findbyid = DemoDropDownSingleSelect()
findbyid.demo_dropdown_single_select()
