# How to navigate to another URL? by using get command but there is no any navigation command in python.
# Navigation commands are very popular in JAVA.
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By  # Imported By from common


@pytest.mark.smoke
def test_vwologin_negative_TC():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    # id-> name-> classname-> tagName-> LinkText/PartialText-> CSS Selector-> XPATH
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username" # suppose this is not available then we will pick "name"
    # data-qa="hocewoqisi">
    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys("admin")  # To enter the text in an input box, we need "send_keys"

    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # aria-autocomplete="list"
    # >
    password_element = driver.find_element(By.ID, "login-password")
    password_element.send_keys("admin")

    # <button
    # type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">
    # <span
    # class="icon loader hidden" d
    # ata-qa="zuyezasugu">
    # </span>
    # <span data-qa="ezazsuguuy">
    # Sign in
    # </span>
    # </button>
    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    time.sleep(5)

    # <div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email, password, IP address or location did not match
    # </div>
    error_msg_element = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"

    driver.quit()
# There are 2 major problems in this case. 1.time.sleep(5) which is wait.Here, we are using python wait
# mechanism.Python interpreter is getting basically weighted.We are telling python interpreter to wait for 5 seconds
# which is not good. 2.Another problem is this code can be made more generic if possible. Generic basically means
# below is the code which we need to execute every time. driver = webdriver.Chrome() driver.get(
# "https://app.vwo.com") And also quit driver.quit() # We need to execute every time. Hence, such kind of code we can
# make it generic where different test cases we have, we can appoint them in a simple manner.

