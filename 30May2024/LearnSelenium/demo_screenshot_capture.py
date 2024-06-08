import time
from selenium.webdriver.common.by import By
from selenium import webdriver


class DemoToCaptureSnaphot:
    def demo_to_capture_snapshot(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.ID, 'login-continue-btn').click()
        driver.get_screenshot_as_png()
        driver.save_screenshot(".\\error0.png")
        driver.get_screenshot_as_file("D:\\ProgramFilesFolder\\error1.png")


findbyid = DemoToCaptureSnaphot()
findbyid.demo_to_capture_snapshot()
