import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_01_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]').click()
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Vandana")
    alert.accept()
    time.sleep(5)

    # How to verify the message in this example "Vandana" ? ]
    result = driver.find_element(By.ID, 'result')
    print(result.text)
    assert "Vandana" in result.text
# Steps need to remember:
# 1.Wait for the alert
# 2.switch_to.alert
# 3.If it can take input then use "send keys" else not.
# 4.At the end, accept or dismiss (Perform the action)

# There are 2 types of pop ups:
# 1.Normal Model or html pop up--> For this, We have to wait for the model to come and click on the escape button, or close button.
# Strategy is same like alerts.


# 2.alerts which we can handle by above strategy
