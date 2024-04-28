import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


def test_01_actions():
    driver = webdriver.Chrome()
    # driver.get("https://awesomeqa.com/practice.html")
    # first_name = driver.find_element(By.NAME, 'firstname')

    # To use Action class, We need to create an object of Action Chain Class.
    # actions = ActionChains(driver)  # We need to pass the driver in this case.

    # we want to send keys but with the shift keys
    # actions \
    #     .key_down(Keys.SHIFT) \
    #     .send_keys_to_element(first_name, "Vandana") \
    #     .key_up(Keys.SHIFT) \
    #     .perform()


    # key_down means which key we want to press? I want to press SHIFT then which element I want to send?
    # I want to send first name with value "vandana" then I need to release my key.

    # for eg: I am typing vandana (normal)
    # If I press SHIFT then I type VANDANA
    # then I want to release the key which is key_up now and post that if I type it will become normal like VANDANAppppp

    # press SHIFT key down
    # press SHIFT key up (release)
    # url = driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Download File']")
    # actions.context_click(url).perform() # which element you want to context element? url. perform will do all the activity.
    actions = ActionChains(driver)
    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions.send_keys("Selenium").perform() # why directly it will work? because when we load the page cursor will automatically present. So, in this case, autofocus is happening.
    time.sleep(20)
