from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Payment(BasePage):
    header = 'Please choose your payment method'
    by_check = 'Pay by check'
    by_bank_wire = 'Pay by bank wire'

    def __pay_by_method(self, payment_method):
        xpath = '//*[@title="' + payment_method + '"]'
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, xpath))
        )
        checkout_button = self.driver.find_element_by_xpath(xpath)
        checkout_button.click()

    def pay_by_check(self):
        self.__pay_by_method(self.by_check)

    def pay_by_bank_wire(self):
        self.__pay_by_method(self.by_bank_wire)

