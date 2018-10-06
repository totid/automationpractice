from base.BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from pages.ShoppingCartPopupPage import ShoppingCartPopupPage
from pages.ShoppingCartSummary import ShoppingCartSummary
from pages.Authentication import Authentication
from pages.CreateAccount import CreateAccount
from common.common_classes import PersonalInformation
from common.common_classes import Address

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
        user_information = PersonalInformation(email="johndoe@mailinator.com", first_name="John", last_name="Doe", password="12345")
        user_address = Address(address="4374  Traders Alley", city="Kansas City", state="Missouri", postal_code="64106", phone_mobile="8164465964")
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
        cart = ShoppingCartPopupPage(self.browser)
        cart.proceed_to_checkout()
        cart_summary = ShoppingCartSummary(self.browser)
        cart_summary.proceed_to_checkout()
        authentication = Authentication(self.browser)
        authentication.create_an_account(user_information.email)
        c = CreateAccount(self.browser)
        c.register(user_information=user_information, address=user_address)

