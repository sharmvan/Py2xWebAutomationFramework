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

    price_of_product = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    prices = []
    for price in price_of_product:
        print(price.text)
        y = price.text.replace("$", "").strip()
        prices.append(y)

    prices.sort()
    min_price = prices[1]
    print(f"The lowest price of the product is {prices[1]}")
    time.sleep(5)
    driver.quit()

