from base.BaseTest import BaseTest
from pages.HomePage import  HomePage

class FunctionalTests(BaseTest):
    def test_open_page(self):
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)

    def test_search(self):
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        h = HomePage(self.browser)
        h.search_product("PROVA")
        h.search_button()
