from base.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class HomePage(BasePage):
    search_field_by_id = 'search_query_top'
    search_button_by_name = 'submit_search'
    sign_in_button = 'login'
    shopping_cart = "View my shopping cart"
    element_not_found = '.alert'

    def is_shopping_cart_empty(self):
        try:
            self.driver.find_element_by_css_selector(self.element_not_found)
        except NoSuchElementException:
            return False
        return True

    def search_product(self, searched_product):
        element = self.driver.find_element_by_id(self.search_field_by_id)
        element.send_keys(searched_product)

    def search_button(self):
        element = self.driver.find_element_by_name(self.search_button_by_name)
        element.click()

    def sign_in(self):
        element = self.driver.find_element_by_class_name(self.sign_in_button)
        element.click()

    def open_shopping_cart(self):
        xpath = '//*[@title="' + self.shopping_cart + '"]'
        element = self.driver.find_element_by_xpath(xpath)
        element.click()
