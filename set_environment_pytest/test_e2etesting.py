import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_blackberry_product():
    service_obj = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(4)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, 'a[href*="shop"]').click()
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    for product in products:
        productname = product.find_element(By.XPATH, "div/h4/a").text
        if productname == "Blackberry":
            print(productname)
            product.find_element(By.XPATH, "//div[@class='card h-100']/div/button").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys('ind')
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'India')))
    driver.find_element(By.LINK_TEXT,"India").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    success = driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']").text
    assert "Success! Thank you!" in success
    driver.close()
