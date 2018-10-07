from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Shipping(BasePage):
    header = 'Shipping'
    tos = 'cgv'
    proceed_to_checkout_button = 'processCarrier'

    def tos_not_selected(self):
        xpath = "//*[contains(text(), 'You must agree to the terms of service before continuing.')]"
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath))
            )
        except NoSuchElementException:
            return False
        return True

    def click_tos(self):
        tos_checkbox = self.driver.find_element_by_id(self.tos)
        tos_checkbox.click()

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, self.proceed_to_checkout_button))
        )
        checkout_button = self.driver.find_element_by_name(self.proceed_to_checkout_button)
        checkout_button.click()