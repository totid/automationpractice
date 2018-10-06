from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class ShoppingCartSummary(BasePage):
    header = 'cart_title'
    proceed_to_checkout_button = 'standard-checkout'

    def __init__(self, driver):
        super().__init__(driver)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.header))
        )

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME, self.proceed_to_checkout_button))
        )
        checkout_button = self.driver.find_element_by_class_name(self.proceed_to_checkout_button)
        checkout_button.click()
