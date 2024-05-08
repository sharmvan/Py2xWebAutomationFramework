import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_practice():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.maximize_window()
    time.sleep(5)

    driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id="result"]'))

    driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
    time.sleep(2)

    s1 = driver.find_element(locate_with(By.XPATH, '//small[contains(text(),"Username")]').below({By.ID: 'username'}))
    print(s1.text)
    time.sleep(5)

    assert s1 == "Username must be at least 3 characters"
    time.sleep(7)
