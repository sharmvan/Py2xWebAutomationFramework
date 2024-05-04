import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time


def test_02_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    # clickable = driver.find_element(By.ID, "clickable") # clickable is an input box.
    # action = ActionChains(driver)
    # action.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("Vandana").key_up(Keys.SHIFT).perform()
    #
    # # another way:
    # # key_down(Keys.SHIFT)  -- It will be pressing the SHIFT
    # # key_down("A") -- It will be pressing A
    # action.click_and_hold(clickable).key_down(Keys.SHIFT).key_down("A").perform()
    # time.sleep(3)

    # Click means Normal click - we will be able to click on the page and action will get performed.
    # click_and_hold means - click and hold - will not release

    # clickable = driver.find_element(By.ID, "click")
    # ActionChains(driver).click(clickable).perform()
    # time.sleep(2)
    #
    # # If I able to click then I can mention assert
    # assert "resultPage.html" in driver.current_url

    # clickable = driver.find_element(By.ID, "click")
    # ActionChains(driver).click_and_hold(clickable).perform()
    # time.sleep(2)
    # assert "resultPage.html" in driver.current_url

    driver.find_element(By.ID, "click").click()
    # Action Builder -> by using mouse, we can click back also by using Action Builder.
    # Action Builder is used for the mouse buttons.
    action_builder = ActionBuilder(driver)  # we need to pass driver. It provides extra items.
    action_builder.pointer_action.pointer_down(MouseButton.BACK) # by using pointer_action, we can move your mouse to a particular location & you can click a particular button also.
    action_builder.pointer_action.pointer_down(MouseButton.BACK)
    action_builder.perform()
    time.sleep(15)
