# Shadow DOM:ShadowDOM is basically a custom element.
# Sometimes we have HTML elements like: div tag, p tag, input tag, check boxes, radio button, images etc.
# So, this is a custom element where you will be hiding the functionality.

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_01_shadowDOM():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(3)
    driver.maximize_window()
    div = driver.find_element(By.CLASS_NAME, "jackPart")

    # Now we have to scroll the page to come at the input box i.e. "Enter pizza name"
    # To scroll into this, we need some mechanism.
    # so, before shadowDOM , we need something to

    # -scroll to view to div. --> for this, we need to learn JSExecutor (refer lab_038).
    # -then we can handle shadowDOM.
    # -Only then we click on the Pizza.

    # If we directly find it by id or XPATH, this will throw an error because this is shadow root.
    # shadowDOM are of 2 types: open and close
    # open means it can be open.
    # close: we can't handle in selenium but open: we can.
    # pizza=(driver.find_element(By.ID, "pizza"))
    # pizza.send_keys("Farmhouse")

    # Now Lab_038, we can here also write JS code.
    # -scroll to view to div
    js_ex = driver.execute_script
    js_ex("arguments[0].scrollIntoView(true)",div)
    time.sleep(3)

    # but now we need to click on this button. we have to find the pizza.
    # we can find it by using JS executor again here.
    pizza=driver.execute_script("return document.querySelector('div.jackPart').shadowRoot.querySelector('div#app2').shadowRoot.querySelector('input')").send_keys("Farmhouse")

    # We need return because we want to fetch the element (input box). That's why return is important.

    time.sleep(10)
    driver.quit()
# Please Note: whatever the elements are present in "ShadowRoot", we can't find directly like below:
# div = driver.find_element(By.CLASS_NAME, "jackPart")
# we need to execute JS code here to find the elements.
