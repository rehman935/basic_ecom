import time

from selenium.webdriver.common.by import By

from PageObjects.checkout_conf import CheckoutConf
from Utils.BrowserUtils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, 'a[href*="shop"]')
        self.product_carts = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_carts)
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == product_name:
                print(productName)
                product.find_element(By.XPATH, "div/button").click()
                time.sleep(3)

    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout = CheckoutConf(self.driver)
        return checkout


