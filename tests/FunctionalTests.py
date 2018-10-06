from base.BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from pages.CartPopupPage import CartPopupPage


class FunctionalTests(BaseTest):
    def test_open_page(self):
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)

    def test_search_not_existing_product(self):
        product = "prova"
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.search_product(product)
        home_page.search_button()
        search_results = SearchPage(self.browser)
        res = search_results.product_not_found()
        self.assertTrue(res)

    def test_search_existing_product(self):
        product = "dress"
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.search_product(product)
        home_page.search_button()
        search_results = SearchPage(self.browser)
        res = search_results.product_found()
        self.assertTrue(res)
        search_results.select_list_view()
        search_results.add_to_cart_first_product_found()
        cart = CartPopupPage(self.browser)
        cart.proceed_to_checkout()

