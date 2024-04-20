from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


def test_curo_herokuapp():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")
    driver.maximize_window()
    make_appointment_button = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_button.click()
    driver_title = driver.title
    print(driver_title)
    assert driver_title == "CURA Healthcare Service"
    time.sleep(2)
    element_username = driver.find_element(By.ID, "txt-username")
    element_username.send_keys("John Doe")
    time.sleep(2)
    element_password = driver.find_element(By.ID, "txt-password")
    element_password.send_keys("ThisIsNotAPassword")
    time.sleep(2)
    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()
    time.sleep(2)
    make_appointment = driver.find_element(By.CLASS_NAME, "col-sm-12")
    print(make_appointment.text)
    assert make_appointment.text == "Make Appointment"
