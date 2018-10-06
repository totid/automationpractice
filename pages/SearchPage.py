from base.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class SearchPage(BasePage):
    element_not_found = '.alert'
    list = 'list'
    grid = 'grid'
    add_to_cart_button = 'ajax_add_to_cart_button'

    def product_not_found(self):
        try:
            self.driver.find_element_by_css_selector(self.element_not_found)
        except NoSuchElementException:
            return False
        return True

    def product_found(self):
        return not self.product_not_found()

    def select_list_view(self):
        self.driver.find_element_by_id(self.list).click()

    def select_grid_view(self):
        self.driver.find_element_by_id(self.grid).click()

    def __get_all_elements(self):
        return self.driver.find_elements_by_class_name(self.add_to_cart_button)

    def add_to_cart_first_product_found(self):
        self.add_product_to_cart(0)

    def add_product_to_cart(self, index):
        self.__get_all_elements()[index].click()

