# Windows: Suppose we have open an URL and on the same open uRL, we have a link and when we click on
# that link, a new window will open.
# Parent window, child window.
# when ypu open this link: "https://the-internet.herokuapp.com/windows"
# While opening this link, when you will "click here" button, a new window will get open.
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time


def test_window():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    time.sleep(2)

    # before clicking "click here" button:
    main_window_handle = driver.current_window_handle # This is our parent window.
    print(main_window_handle)
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()  # A child window will get opened

    window_handles = driver.window_handles  # It will give you Total window_handle. in this case: 2 (parent & child)
    print(window_handles)
    time.sleep(2)


    # How to navigate to second window? by using for loop in "window_handles"
    for handle in window_handles:
    # we can switch to any window by using "switch_to.window" method. and which window ypu want to do "handle" in this case.
        driver.switch_to.window(handle) # switch to child
        time.sleep(10)
        if "New Window" in driver.page_source:
            print("Found the text")
            break


# Note: Navigations happen when you are on the same page. but here there are 2 windows.

    # After 3 seconds, if we want to move back to parent window then use "switch_to.window"?
    time.sleep(3)
    driver.switch_to.window(main_window_handle)
    time.sleep(10)






