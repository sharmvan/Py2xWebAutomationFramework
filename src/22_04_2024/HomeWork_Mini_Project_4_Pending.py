import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.ebay
@allure.title("Verify the the Top 60 Results with there Name and price")
@allure.description("TC#1 - cheapest one from the list.")
def test_ebay():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/")
    driver.maximize_window()
    # time.sleep(2)

    search_box = driver.find_element(By.XPATH, "//input[@id='gh-ac']").send_keys('16gb')
    # time.sleep(2)
    search_btn = driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()
    # time.sleep(2)

    list_of_products = driver.find_elements(By.XPATH, "//span[@role='heading']")

    for product in list_of_products:
        print(product.text)

    list_of_products_price = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    prices = []
    for price in list_of_products_price:
        print(price.text)
        # y = price.replace("$", "").strip()
        prices.append(price)

    prices.sort()
    lowest_price = prices[0]
    print(lowest_price)
    time.sleep(5)
    driver.quit()
