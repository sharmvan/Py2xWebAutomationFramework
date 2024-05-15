# Responsibility of Dashboard class: Verify the username
from selenium import webdriver
from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    user_logged_in = (By.XPATH,"//span[@data-qa='lufexuloga']")

    def get_user_looged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    # page Action
    def get_user_logged_in_text(self):
        return self.get_user_logged_in_text()

    def user_logged_in_text(self):
        return self.get_user_logged_in_text()








