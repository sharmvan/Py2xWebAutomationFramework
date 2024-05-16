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
    username = (By.XPATH, "//input[@id='login-username']")  # username of current class.
    password = (By.XPATH, "//input[@name='password']")
    submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    # forgot_password_button = (By.XPATH, "//button[@onclick='login.gotoForgotPasswordView()']")
    error_message = (By.XPATH, "//div[@id='js-notification-box-msg']")

    free_trail = (By.XPATH, "//a[@class='text-link']")

    # sso_login = (By.XPATH, "//button[@onclick='login.goToSSOView()']")
    # remember_checkbox = (By.XPATH, "//label[@for='checkbox-remember']")

    # Proper "Page Action" is needed so that we can interact with "page locators" in the future.
    # Here we will be creating a couple of utilities and anyone can use this utility if they want to get in the future.
    # If we want to get username, we can use "driver.find_element" by login.
    def get_username(self):  # To access the username, I can use a function called as "get_username"
        return self.driver.find_element(*LoginPage.username)  # * means current class. username of current class.

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def get_free_trail(self):
        return self.driver.find_element(*LoginPage.free_trail)

    # Page Action --> Main Action.
    # This page can do one main action i.e. It can do log in.
    # We need to pass usr and pwd. whatever the usr and pwd, you will pass me.
    # I will use "get_username()" and I will do "send keys".
    def login_to_vwo(self, usr, pwd):  # This is for +ve and -ve both
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

    def click_free_trail(self):
        self.get_free_trail().click()
