import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a(self):
        driver = self.driver 
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(4)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(4)

    # Add to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(4)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(4)

    # remove item and check-out
        driver.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(3)
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(3)
        driver.find_element(By.ID, "checkout").click()
        time.sleep(4)

    # Filling form
        driver.find_element(By.ID, "first-name").send_keys("Johan")
        time.sleep(2)
        driver.find_element(By.ID, "last-name").send_keys("Chandra")
        time.sleep(2)
        driver.find_element(By.ID, "postal-code").send_keys("13430")
        time.sleep(4)
        driver.find_element(By.ID, "continue").click()
        time.sleep(4)
        driver.find_element(By.ID, "finish").click()
        time.sleep(4)

    # back home and Logout 
        driver.find_element(By.ID, "back-to-products").click()
        time.sleep(2)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

