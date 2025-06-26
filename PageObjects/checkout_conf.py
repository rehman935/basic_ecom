from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utils.BrowserUtils import BrowserUtils


class CheckoutConf(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_add = (By.XPATH, "//button[@class='btn btn-success']")
        self.address = (By.CSS_SELECTOR, "input[type='text']")

        self.selectedAddress = (By.LINK_TEXT, "India")
        self.privacyPolicy = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchase = (By.CSS_SELECTOR, "input[type='submit']")
        self.success_msg = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")

    def checkout(self):
        self.driver.find_element(*self.checkout_add).click()

    def enter_deleviry_address(self,countryName):
        self.driver.find_element(*self.address).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.selectedAddress))
        self.driver.find_element(*self.selectedAddress).click()
        self.driver.find_element(*self.privacyPolicy).click()
        self.driver.find_element(*self.purchase).click()

    def validate_address(self):
        success = self.driver.find_element(*self.success_msg).text
        assert "Success! Thank you!" in success


