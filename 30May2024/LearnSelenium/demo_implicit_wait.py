import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoImplicitWait:
    def demo_implicit_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://login.salesforce.com/?locale=in")
        driver.maximize_window()
        time.sleep(2)
        driver.implicitly_wait(10)

        # 1st scenario: Suppose incorrect username and it will wait for 10 sec to find the locator.
        # driver.find_element(By.ID, 'userame').send_keys("Vandana@gmail.com")

        # 2nd scenario: Suppose username is correct then it won't wait for 10 sec.
        # driver.find_element(By.ID, 'username').send_keys("Vandana@gmail.com")

        # 3rd scenario: For correct username, it will not wait for 10 sec.
        #               For incorrect pwd, it will wait for 10 sec.
        # driver.find_element(By.ID, 'username').send_keys("Vandana@gmail.com")
        # driver.find_element(By.ID, 'passwrd').send_keys("9874555")

        # 4th scenario: For correct username, it will not wait for 10 sec.
        #               For correct pwd, it will wait not for 10 sec.
        driver.find_element(By.ID, 'username').send_keys("Vandana@gmail.com")
        driver.find_element(By.ID, 'password').send_keys("9874555")

        # Note: If something is correct, it will not wait and proceed further.
        #       If something is incorrect, only then it will wait for 10 seconds.


findbyid = DemoImplicitWait()
findbyid.demo_implicit_wait()
