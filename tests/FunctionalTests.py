from base.BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


class FunctionalTests(BaseTest):
    def test_open_page(self):
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)

    def test_search_not_existing_product(self):
        product = "prova"
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        h = HomePage(self.browser)
        h.search_product(product)
        h.search_button()
        s = SearchPage(self.browser)
        res = s.product_not_found()
        self.assertTrue(res)

    def test_search_existing_product(self):
        product = "blouse"
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        h = HomePage(self.browser)
        h.search_product(product)
        h.search_button()
        s = SearchPage(self.browser)
        res = s.product_found()
        self.assertTrue(res)

