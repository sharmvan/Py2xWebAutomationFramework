import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time


def test_03_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # Here we are using Action Chains. Action builder is just for mouse & maximum time we will be using Action Chains only.
    # If we want to double click on the same item.
    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver).double_click(clickable).perform()
    time.sleep(2)
