import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time


def test_04_move_to_element():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Here we are using Action Chains. Action builder is just for mouse & maximum time we will be using Action Chains only.
    # If we want to double-click on the same item.
    hover = driver.find_element(By.ID, "hover")
    ActionChains(driver).move_to_element(hover).perform()
    time.sleep(2)


def test_04_DragAndDrop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    drag = driver.find_element(By.ID, "draggable")
    drop = driver.find_element(By.ID, "droppable")
    ActionChains(driver).drag_and_drop(drag, drop).perform()
    time.sleep(3)


def test_04_scroll():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    iframe = driver.find_element(By.NAME, "nested_scrolling_frame")
    # iframe = driver.find_element(By.TAG_NAME, "iframe")-- We can use tag name as well as we have one frame only.
    ActionChains(driver).scroll_to_element(iframe).perform()
    time.sleep(100)


def test_05_WheelScroll():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    iframe = driver.find_element(By.NAME, "nested_scrolling_frame")
    ActionChains(driver).scroll_to_element(iframe).perform()
    time.sleep(100)


# scroll from an element (iframe in this case) with the offset particular amount (0-50: x y coordinate)
def test_06_scrollFromElement_WithOffsetAmount():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    time.sleep(2)

    # In this code, from the iframe, I want to scroll 200 y from o to y.
    # There is a frame in the frame itself, we want to scroll. so, we will use "scroll_from_origin"
    # from the iframe to 200 pixel we want to do that.
    # Hence, if there is a certain situation, where you have a iframe, in the iframe only, you want to scroll
    # from an element, then you can perform below action.
    iframe = driver.find_element(By.NAME, "nested_scrolling_frame")
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(driver).scroll_from_origin(scroll_origin, 0, 200).perform()
    time.sleep(100)


def test_07_makemytrip():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    time.sleep(5)
    from_city = driver.find_element(By.ID, "fromCity")
    #from_city.send_keys("New Delhi") --> This is not a good way and not recommended
    #Rather than using send keys, we can use action classes
    #Below is the good way as first we want to hover. For eg:
    #We have an input box, we will come here in input box, then we want to click, then send keys and perform
    #whenever there are certain input boxes which are out of focus, we will kove to a particulatr element,
    #and then "ActionChains" in this case.
    #when we can use this? when directly "send_keys" not working.
    action = ActionChains(driver).move_to_element(from_city).click().send_keys("New Delhi").perform()
    time.sleep(20)
    