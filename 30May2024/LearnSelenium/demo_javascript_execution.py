import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoJavaScriptExecution:
    def demo_javascript_execution(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(8)
        # driver.get("https://www.yatra.com/")
        # driver.execute_script("window.open('https://www.yatra.com/')")
        driver.execute_script("window.open('https://www.yatra.com/','_self');")
        time.sleep(3)
        # web_element = driver.execute_script("return document.getElementsByTagName('img')[3];")
        # time.sleep(3)
        web_element = driver.execute_script("return document.getElementsByClassName('VueCarousel-slide slide package super-offer eventTrackable js-prodSpecEvtCat')[0];")
        driver.execute_script("arguments[0].click();", web_element)
        time.sleep(8)


findbyid = DemoJavaScriptExecution()
findbyid.demo_javascript_execution()

