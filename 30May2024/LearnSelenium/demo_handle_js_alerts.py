import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoHandleJSAlerts:
    def demo_handle_js_alerts(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame("iframeResult")
        time.sleep(2)
        driver.find_element(By.XPATH, '//button[@onclick="myFunction()"]').click()
        time.sleep(2)
        # # Accept or Ok alert
        # driver.switch_to.alert.accept()
        # time.sleep(2)

        # # Dismiss Alert
        # driver.switch_to.alert.dismiss()
        # time.sleep(2)

        # To get the Text
        print(driver.switch_to.alert.text)
        # Send Keys Alert
        driver.switch_to.alert.send_keys("Vandana")
        # driver.switch_to.alert.accept() # We can write this statement with below as well.
        Alert(driver).accept()
        time.sleep(2)


findbyid = DemoHandleJSAlerts()
findbyid.demo_handle_js_alerts()
