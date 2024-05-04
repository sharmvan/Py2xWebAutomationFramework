import time, allure, pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@allure.title("Verify that login is working")
@allure.description("TC#1 Simple login check on flipkart.com")
def test_SvgElements():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    time.sleep(5)
    list_of_states=driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in list_of_states:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break # To stop the execution
    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name="svg_elements", attachment_type=AttachmentType)
    driver.quit()



