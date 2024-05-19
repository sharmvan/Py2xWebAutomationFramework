# Webdriver fixture example
import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()  # Call load_dotenv function


@pytest.fixture(scope="class")  # this fixture will be available in any class.
def setup(request):  # It will take an argument know as "request"
    driver = webdriver.Chrome()
    driver.maximize_window()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")

    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password
    request.cls.base_url = base_url

    yield driver
    driver.quit()
