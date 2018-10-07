from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Addresses(BasePage):
    header = 'Addresses'
    proceed_to_checkout_button = 'processAddress'

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, self.proceed_to_checkout_button))
        )
        checkout_button = self.driver.find_element_by_name(self.proceed_to_checkout_button)
        checkout_button.click()
