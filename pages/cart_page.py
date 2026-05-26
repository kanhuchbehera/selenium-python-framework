from selenium.webdriver.common.by import By

class CartPage:

    checkout_btn = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(*self.checkout_btn).click()