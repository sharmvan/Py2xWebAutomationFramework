# In Selenium 4:
from selenium import webdriver  # directly call webdriver. No need to install drivers (chrome, edge, firefox etc) if you have install chome, edge in your system.


def test_open_vwologin():
    driver = webdriver.Edge()  # Call chrome by using webdriver. No need to set up the path
    driver.get("https://app.vwo.com") # This command I have open. It will wait for sometime and after that it will automatically close.
# When I run this, It will be automatically closed. but how as we have not written code of "close"?
# After sometimes when there is no next command, it will get automatically closed and Python Interpreter is responsible to close it.
# Python Interpreter is optimized if there is no command, it will stop the execution.
# Python Interpreter basically do it one by one line.