# Exception: is something which will interrupt your program. We can handle it by using try
# and accept.

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(2)
    try:
        driver.find_element(By.NAME,"o").send_keys("The Testing Academy")
        time.sleep(2)
    except NoSuchElementException as nse:
        print(f"no such element: Unable to locate element: {nse}")
    time.sleep(2)
    driver.quit()
