# How to navigate to another URL? by using get command but there is no any navigation command in python.
# Navigation commands are very popular in JAVA.

import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By  # Imported By from common


@pytest.mark.smoke
@allure.title("Verify thet login is working in cura website")
@allure.description("TC#1 - Simple Login check on CURA katalon website.")
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    # Suppose we have this below element:
    # <input type="email" class="text-input W(100%)" name="username" data-qa="hocewoqisi">

    # <input
    # type="email"
    # class="text-input W(100%)" # It's not static. It's dynamic.W(100%)--> It will change. for eg: if you
    #                              open this page in IPAD, it will become W(100%).
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >

    # XPATH: All below-mentioned XPATHs are called "Relative XPATHs". Absolute paths are not recommended.

    # //input[@id="login-username"] -- If id is not available then we will use name.
    # //input[@name="username"] -- If name is not available then we will use class. but it's not static. It's dynamic.
    # //input[@class="text-input W(100%)"] -- Not recommended
    # //input[@type="email"] -- this is also not recommended because "type="email"", we will have multiple elements.
    # //input[@data-qa="hocewoqisi"] -- This is custom element. we can use this. "hocewoqisi" -> unique value
    # -- Custom element means if anything user has it.

    make_appointment_btn = driver.find_element(By.XPATH, "//input[@name='username']")
    make_appointment_btn.send_keys("admin")

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)

    driver.quit()








