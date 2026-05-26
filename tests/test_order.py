from utils.browser import start_browser
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


driver = start_browser()

driver.get("https://www.saucedemo.com")

login = LoginPage(driver)
login.login("standard_user", "secret_sauce")

product = ProductPage(driver)
product.add_product()
product.open_cart()

cart = CartPage(driver)
cart.checkout()

checkout = CheckoutPage(driver)
checkout.place_order()

print("Order placed successfully")

driver.quit()