import pytest
import selenium
import time
from selenium import webdriver
from tests.pageObjects.loginPage_pf import LoginPage
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv


@allure.epic("VWO App")
@allure.feature("Login Test")
class VWO_login:
    load_dotenv()


@allure.epic("VWO Login Test")
@allure.feature("TC#0 - VWO App Negative Test")
@pytest.mark.usefixtures("setup")
@pytest.mark.negative
def test_vwlogin_pf_negative(self, setup):
    driver = setup
    driver.get(self.base_url)
    loginpage = LoginPage(driver)
    loginpage.login_to_vwo(user=self.username, pwd="12354654")
    time.sleep(5)
    if "Dashboard" not in driver.title:
        allure.attach(self.driver.get_screenshot_as_png(), name="testloginscreenshot",attachment_type=AttachmentType.PNG)

    assert "Dashboard2" in driver.title
    time.sleep(2)

@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
@pytest.mark.usefixtures("setup")
@pytest.mark.positive
def test_vwlogin_pf_positive(self, setup):
    driver = setup
    driver.get(self.base_url)
    loginpage = LoginPage(driver)
    loginpage.login_to_vwo(user=self.username, pwd=self.password)
    time.sleep(5)
    assert "Dashboard" in driver.title
    time.sleep(2)

