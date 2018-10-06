from base.BasePage import BasePage


class HomePage(BasePage):
    search_field_by_id = 'search_query_top'
    search_button_by_name = 'submit_search'

    def search_product(self, searched_product):
        element = self.driver.find_element_by_id(self.search_field_by_id)
        element.send_keys(searched_product)

    def search_button(self):
        element = self.driver.find_element_by_name(self.search_button_by_name)
        element.click()
