from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DemoFluentWait:
    def demo_fluent_wait(self):
        driver = webdriver.Chrome()
        driver.get("https://login.salesforce.com/?locale=in")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10, 2, ignored_exceptions=[ElementClickInterceptedException])
        wait.until(EC.element_to_be_clickable((By.ID, 'username'))).send_keys("Vandana@gmail.com")
        wait = WebDriverWait(driver, 10, 2, ignored_exceptions=[ElementClickInterceptedException])
        wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys("9874555")


findbyid = DemoFluentWait()
findbyid.demo_fluent_wait()
