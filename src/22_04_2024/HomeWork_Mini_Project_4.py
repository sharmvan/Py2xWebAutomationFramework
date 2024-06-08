# Selenium Mini Project #4
# Open ebay.com.
# Search for the "16 gb"
# Print all the Top 60 Results with their Name and price.
# Give me the cheapest one from the list.
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
    # Search with "16 gb" text    # Get the ITEM Name
    driver.find_element(By.XPATH, "//input[@id='gh-ac']").send_keys('16gb')
    # time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()
    # time.sleep(2)
    # Get the ITEM Name
    list_of_products = driver.find_elements(By.XPATH, "//span[@role='heading']")
    print(type(list_of_products))

    # For loop will fetch all the top 60 item title names
    for index, product_name in enumerate(list_of_products[1:62]):
        items_title_name = product_name.text
        print(index, "", items_title_name)

    # Get the ITEM Prices
    list_of_products_price = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    prices = []

    # For loop will fetch all the top 60 Item prices
    for index, product_price in enumerate(list_of_products_price[1:62]):
        items_price_name = product_price.text
        print(index, "", items_price_name)
        if 'to' in items_price_name:  # get the first price when the price is having Range
            get_only_value = items_price_name.split("to")[0].replace("$", " ").strip()
            print("price is: ", get_only_value)
            price_float = float(get_only_value)
            prices.append(price_float)
        else:  # get the price when item having single price
            # store the price after remove "$" sign and extra space
            get_only_value = items_price_name.replace("$", '').strip()
            price_float = float(get_only_value)
            prices.append(price_float)
    lowest_Price = min(prices)
    print("Lowest price is:", lowest_Price)
