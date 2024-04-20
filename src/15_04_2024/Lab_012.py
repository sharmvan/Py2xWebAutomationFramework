# How to navigate to another URL? by using get command but there is no any navigation command in python.
# Navigation commands are very popular in JAVA.
from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://bing.com/chat")
    time.sleep(25)  # It means wait.you are telling to python interpreter that we have to wait for 25 seconds before
    # moving to next command i.e. line 30. you are not telling to webdriver.you are telling to python interpreter
    driver.get("https://google.com")  # after 25 seconds, I can go to another url.
    # get command is used to navigate to different URL as well.
    print(driver.title)
