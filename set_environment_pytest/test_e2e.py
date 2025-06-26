import json

import os.path
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.shop import ShopPage


from PageObjects.login import LoginPage

data_file = "../data/test_e2e.json"

with open(data_file) as f:
    #convert entire json object into python object
    test_data = json.load(f)
    test_list = test_data["data"]
@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser_instance,test_list_item):
    driver = browser_instance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    login_page = LoginPage(driver)


    shop_page = login_page.login(test_list_item["username"], test_list_item["userpassword"])
    shop_page.add_product_to_cart(test_list_item["mobile"])
    checkout = shop_page.goToCart()
    checkout.checkout()
    checkout.enter_deleviry_address("Ind")
    checkout.validate_address()

