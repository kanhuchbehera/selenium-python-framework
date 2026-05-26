from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    first = (By.ID, "first-name")
    last = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def place_order(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first)
        ).send_keys("Kanhu")

        self.driver.find_element(*self.last).send_keys("Behera")
        self.driver.find_element(*self.zip_code).send_keys("560067")

        self.driver.find_element(*self.continue_btn).click()

        # wait for overview page
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_btn)
        ).click()