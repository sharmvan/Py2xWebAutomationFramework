import os, time, allure, openpyxl, pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)

# Data Driven Test case for the Login Page.
# We will test invalid logins for the vwo login page.

# To make data driven, we need to prepare data in Excel.
# Which library we have used for our Excel automation in python? --> Openpyxl

