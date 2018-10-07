from selenium.common.exceptions import WebDriverException
from base.BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from pages.ShoppingCartPopupPage import ShoppingCartPopupPage
from pages.ShoppingCartSummary import ShoppingCartSummary
from pages.Authentication import Authentication
from pages.CreateAccount import CreateAccount
from pages.MyAccount import MyAccount
from pages.Addresses import Addresses
from pages.Shipping import Shipping
from pages.Payment import Payment
from pages.OrderSummary import OrderSummary
from common.common_classes import PersonalInformation
from common.common_classes import Address


class FunctionalTests(BaseTest):
    def test_open_page(self):
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)

    def test_sign_in_existing_user_from_home_page(self):
        user_information = PersonalInformation(email="johndoe@mailinator.com", first_name="John", last_name="Doe",
                                               password="12345")
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.sign_in()
        authentication = Authentication(self.browser)
        authentication.sign_in(user=user_information)
        account = MyAccount(self.browser)

    def test_search_not_existing_product(self):
        product = "not existing product"
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
        user_information = PersonalInformation(email="johndoe@mailinator.com", first_name="John", last_name="Doe",
                                               password="12345")
        user_address = Address(address="4374  Traders Alley", city="Kansas City", state="Missouri", postal_code="64106",
                               phone_mobile="8164465964")
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

    def test_search_existing_product_sign_in_existing_user(self):
        product = "dress"
        user_information = PersonalInformation(email="johndoe@mailinator.com", first_name="John", last_name="Doe",
                                               password="12345")
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.sign_in()
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
        authentication.sign_in(user=user_information)
        addresses = Addresses(self.browser)
        addresses.proceed_to_checkout()
        shipping = Shipping(self.browser)
        shipping.click_tos()
        shipping.proceed_to_checkout()
        payment = Payment(self.browser)
        payment.pay_by_bank_wire()
        order_summary = OrderSummary(self.browser)
        order_summary.confirm()

    def test_search_existing_product_sign_in_existing_user_not_tos(self):
        product = "dress"
        user_information = PersonalInformation(email="johndoe@mailinator.com", first_name="John", last_name="Doe",
                                               password="12345")
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.sign_in()
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
        authentication.sign_in(user=user_information)
        addresses = Addresses(self.browser)
        addresses.proceed_to_checkout()
        shipping = Shipping(self.browser)
        shipping.proceed_to_checkout()
        self.assertTrue(shipping.tos_not_selected())


