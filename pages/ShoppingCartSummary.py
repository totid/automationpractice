from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


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

    def product_correctly_inserted(self, product):
        try:
            product_name = product.name
            sku_string = "SKU : " + product.sku + ""
            information_string = "Color : " + product.color + ", Size : " + product.size + ""
            self.driver.find_element_by_xpath("//*[contains(text(), '" + product_name + "')]")
            self.driver.find_element_by_xpath("//*[contains(text(), '" + sku_string + "')]")
            self.driver.find_element_by_xpath("//*[contains(text(), '" + information_string + "')]")
        except NoSuchElementException:
            return False
        return True

