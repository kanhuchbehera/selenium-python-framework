from selenium.webdriver.common.by import By

class ProductPage:

    add_bag = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        self.driver.find_element(*self.add_bag).click()

    def open_cart(self):
        self.driver.find_element(*self.cart).click()