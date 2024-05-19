# Page Locators
# Page Actions
# Webdriver - Init
# Custom Functions
# No Assertion here (They are not test cases)
# Page Class
from seleniumpagefactory.Pagefactory import PageFactory


class LoginPage(PageFactory):  # It will inherit from PageFactory. This is single inheritance.
    # Webdriver - Init
    def __init__(self, driver):
        self.driver = driver

    # now we will keep the Locators in the Dictionary Format of tuple
    locators = {
        'username': ('By.XPATH', "//input[@id='login-username']"),  # username of current class.
        'password': ('By.XPATH', "//input[@name='password']"),
        'submit_button': ('By.XPATH', "//button[@id='js-login-btn']"),
        # forgot_password_button = (By.XPATH, "//button[@onclick='login.gotoForgotPasswordView()']")
        'error_message': ('By.XPATH', "//div[@id='js-notification-box-msg']")

        # 'free_trail': ('By.XPATH', "//a[@class='text-link']")

    }

    def login_to_vwo(self, user, pwd):  # This is for +ve and -ve both
        self.username.set_text(user)
        self.password.set_text(pwd)
        self.submit_button.click_button()

    def error_msg(self):
        return self.error_message.get_text()
# https://selenium-page-factory.readthedocs.io/en/latest/
# Extended WebElements Methods
# set_text	get_text
# clear_text	click_button
# double_click	get_list_item_count
# select_element_by_text	select_element_by_index
# select_element_by_value	get_all_list_item
# get_list_selected_item	highlight
# is_Enabled	is_Checked
# getAttribute	hover
# visibility_of_element_located	invisibility_of_element_located
# element_to_be_clickable	execute_script
# context_click	text_to_be_present_in_element
# click_and_hold	release