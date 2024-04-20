# Selenium that helps to automate the browsers.
# Selenium 3-> 20% people use selenium 3 --> We had JSON wire protocol
# Selenium 4-> 70% people have been migrated to selenium 4 --> Here we have W3C protocol and one more feature added: Selenium Manager
# We also will be using Selenium 4 only.
# Major difference between Selenium 3 & Selenium 4 in terms of code.
# Selenium manager says that the moment you install "pip install selenium", and the version is greater than 4.x then you
# don't have to set up the browser drivers

# In Selenoum 3, previously we used to do below to set the path first to open a simple URL:
from selenium import webdriver


def test_open_website():
    driver_path = "C:\Users\Sharmvan\Downloads\edgedriver_win64"  # driver_path--you have downloaded
    driver = webdriver.EdgeService(executable_path=driver_path)  # to get driver instance
    driver.get("https://app.vwo.com")  # use the command of the driver

# But Below part is not needed nowadays in selenium 4:
# driver_path = "C:\Users\Sharmvan\Downloads\edgedriver_win64"  # driver_path--you have downloaded
# driver = webdriver.EdgeService(executable_path=driver_path)  # to get driver instance
