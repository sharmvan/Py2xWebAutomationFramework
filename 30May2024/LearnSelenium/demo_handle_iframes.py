import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoHandleIFrames:
    def demo_handle_Iframes(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        time.sleep(5)

        # # switch with iframe locator
        # driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="iframeResult"]'))

        # # switch with id
        # driver.switch_to.frame("iframeResult")

        # switch with name
        driver.switch_to.frame("iframeResult")
        
        # switch with index
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH,
                            '//div[@class="tnb-right-section"]//a[@aria-label="Sign Up to Improve Your Learning Experience"]').click()
        time.sleep(5)


findbyid = DemoHandleIFrames()
findbyid.demo_handle_Iframes()
