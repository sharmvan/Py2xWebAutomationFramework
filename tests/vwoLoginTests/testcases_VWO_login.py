# In this, we will write our test cases. We can add "assertions" also.
import time

import allure
import pytest
from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage


# Fixtures function can be used as test data. They can be executed some of the tasks before you do anything else.
# Fixtures are something which can be injected into the test cases.
@pytest.fixture()
def setup():  # we need to setup the driver. From where the driver will come? So, we can use a setup function.
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver

# driver = setup
# loginPage = LoginPage(driver) -- means when we call this class i.e."LoginPage", we are passing the driver.
# This drive (line:20) is getting passed to this "LoginPage" because "LoginPage" also need this to find the element (loginPage: line no: 43)
# Meant to say whatever the driver you will pass, I will keep this into this variable (self.driver).

@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup  # We will get driver from setup. Fixture will give us the driver.
    loginPage = LoginPage(
        driver)  # I will call LoginPage and we will pass the driver. We have to import the "LoginPage" class.
    loginPage.login_to_vwo(usr="admin@gmail.com", pwd="admin")
    time.sleep(5)
    error_message = loginPage.get_error_message_text()
    assert error_message == "Your email, password, IP address or location did not match"


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(usr="py2x@thetestingacademy.com", pwd="Wingify@1234")
    time.sleep(10)
    dashboardPage=DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "Aman" in dashboardPage.user_logged_in_text()
