from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Responsibility of Login class:
# get username and send keys - email
# get password and send keys - email
# click the submit button and navigate to dashboard page
# for invalid test cases, error message, for get password. I have just returned the Responsibility.


# 1st thing is created a class
# self is a default variable in the class. It is an object itself. It points to class as all below created functions
# belong to class.
class LoginPage:
    def __init__(self, driver):  # This is parameterized constructor. Not a default constructor
        self.driver = driver

    # Explanation of above created function:
    # If whatever the driver you will set, I will set the driver to myself.
    # page object class says that if you are not using certain page objects as of now. mark them as commented and don't add them into page object class.
    # Second thing is page locator. How can we keep our page locators?
    # We have just the found locators. and these are just normal tuples. we need to create them into Actions.
    # Proper page action are needed.
    username = (By.ID, "login-username")  # username of current class.
    password = (By.ID, "login-password")
    sign_in_btn = (By.ID, "js-login-btn")
    # forget_password = (By.XPATH, "//button[@class='btn btn--link btn--primary Td(u) Fz(12px)']")
    error_msg = (By.XPATH, "//div[@id='js-notification-box-msg']")

    # free_trail = (By.XPATH, "//a[@class='text-link']")
    # sso_login = (By.XPATH, "//button[@class='btn btn--link btn--primary Td(u)']")
    # remember_checkbox = (By.XPATH, "//span[@class='checkbox-radio-button ng-scope']")

    # Proper "Page Action" is needed so that we can interact with "page locators" in the future.
    # Here we will be creating a couple of utilities and anyone can use this utility if they want to get in the future.
    # If we want to get username, we can use "driver.find_element" by login.
    def get_username(self):  # To access the username, I can use a function called as "get_username"
        return self.driver.find_element(*LoginPage.username)  # * means current class. username of current class.

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_error_msg(self):
        return self.driver.find_element(*LoginPage.error_msg)

    def get_sign_in_btn(self):
        return self.driver.find_element(*LoginPage.sign_in_btn)


# This function can be used for +ve and -ve both.
    def vwo_login(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_password().click()

    def get_error_msg_text(self):
        return self.get_error_msg().text

    # Page Action --> Main Action.
    # This page can do one main action i.e. It can do log in.
    # We need to pass usr and pwd. whatever the usr and pwd, you will pass me.
    # I will use "get_username()" and I will do "send keys".
    def login_to_vwo(self, usr, pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_sign_in_btn().click()

    def get_error_message_text(self):
        return self.get_error_msg().text
