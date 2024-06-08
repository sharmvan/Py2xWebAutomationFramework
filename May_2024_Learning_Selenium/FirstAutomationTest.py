# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get("https://training.rcvacademy.com/")
# driver.maximize_window()
# time.sleep(25)
# print(driver.title)
# driver.quit()


# from selenium import webdriver
# import time
# driver = webdriver.Firefox()
# driver.get("https://training.rcvacademy.com/")
# driver.maximize_window()
# time.sleep(25)
# print(driver.title)
# driver.quit()


# from selenium import webdriver
# import time
# driver = webdriver.Edge()
# driver.get("https://training.rcvacademy.com/")
# driver.maximize_window()
# time.sleep(25)
# print(driver.title)
# driver.quit()


# "Ie" Not install my system. That's why it's throwing an error.
from selenium import webdriver
import time
driver = webdriver.Ie()
driver.get("https://training.rcvacademy.com/")
driver.maximize_window()
time.sleep(25)
print(driver.title)
driver.quit()
