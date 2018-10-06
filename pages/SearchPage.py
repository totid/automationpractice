from base.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class SearchPage(BasePage):
    element_not_found = '.alert'

    def product_not_found(self):
        try:
            self.driver.find_element_by_css_selector(self.element_not_found)
        except NoSuchElementException:
            return False
        return True

    def product_found(self):
        return not self.product_not_found()
