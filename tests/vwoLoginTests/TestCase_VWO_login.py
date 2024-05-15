import allure, time, pytest
from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardPage import DashboardPage


# Assertions
# It can be used as a test data. It can be used to execute some of the tasks before you do anything else.
# It can be something which can be injected into this test case.
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO login Test")
@allure.feature("TC#0 - VWO app Negative Test case")
@pytest.mark.negative
def test_vwo_login_negative(setup):  # We will inject "setup" in both +ve and -ve test cases
    driver = setup  # We will get "driver" from "setup" only. Fixture will give us the driver.
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(usr="admin@admin@gmail.com", pwd="admin")
    time.sleep(5)
    err_msg = loginPage.get_error_msg_text()
    assert err_msg == "Your email, password, IP address or location did not match"


@allure.epic("VWO login Test")
@allure.feature("TC#1 - VWO app positive Test case")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(usr="py2x@thetestingacademy.com", pwd="Wingify@1234")
    time.sleep(10)
    dashboardPage=DashboardPage(driver)
    assert "Dashboard" in driver.title
    #assert "Aman" in dashboardPage.user_logged_in_text()