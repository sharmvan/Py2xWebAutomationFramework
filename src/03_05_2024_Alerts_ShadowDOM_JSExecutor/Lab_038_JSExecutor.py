# Java Script Executor: we can inject any JS code. for eg: Alert.
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_01_JSExecutor():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    driver.maximize_window()

    # suppose this click is not supported.
    # sometimes you won't be able to click by using this below code.
    # Suppose below code is not working then we can use "Java Script code" to click on this button also.
    # driver.find_element(By.XPATH,'//button[@onclick="addElement()"]').click()

    # we can create a JAVA Script code by using "driver.execute_script" function.
    btn=driver.find_element(By.XPATH,'//button[@onclick="addElement()"]')
    js_ex = driver.execute_script  # --This is the function, we can use.
    js_ex("arguments[0].click()",btn)
    js_ex("arguments[0].click()",btn)
    # execute_script takes 2 arguments. what is the script that you want to execute on "btn" element.
    # on this btn, please do click.
    # arguments[0] means replace this (btn) with this (arguments[0]) and execute
    # This is the JS Code that I am executing. Find the button, click arguments[0].click()
    time.sleep(10)
    driver.quit()
