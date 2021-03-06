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
from common.common_classes import Product


class FunctionalTests(BaseTest):
    def test_open_page(self):
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)

    def test_open_shopping_cart_empty_existing_user_not_signed(self):
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.open_shopping_cart()
        self.assertTrue(home_page.is_shopping_cart_empty())

    def test_open_shopping_cart_empty_existing_user_signed(self):
        user_information = PersonalInformation(email="johndoe@mailinator.com", first_name="John", last_name="Doe",
                                               password="12345")
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.sign_in()
        authentication = Authentication(self.browser)
        authentication.sign_in(user=user_information)
        account = MyAccount(self.browser)
        name_surname = user_information.first_name + ' ' + user_information.last_name
        self.assertTrue(account.is_user_logged(name_surname))
        home_page.open_shopping_cart()
        self.assertTrue(home_page.is_shopping_cart_empty())

    def test_product_correctly_inserted_into_cart_user_not_signed_in(self):
        product = "dress"
        p = Product(name="Printed Summer Dress", sku="demo_5", color="Yellow", size="S")
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
        self.assertTrue(cart_summary.product_correctly_inserted(p))

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
        name_surname = user_information.first_name + ' ' + user_information.last_name
        self.assertTrue(account.is_user_logged(name_surname))

    def test_sign_in_existing_user_wrong_password_from_home_page(self):
        user_information = PersonalInformation(email="johndoe@mailinator.com", first_name="John", last_name="Doe",
                                               password="12346")
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.sign_in()
        authentication = Authentication(self.browser)
        authentication.sign_in(user=user_information)
        self.assertTrue(authentication.sign_in_failed())
        account = MyAccount(self.browser)
        name_surname = user_information.first_name + ' ' + user_information.last_name
        self.assertFalse(account.is_user_logged(name_surname))

    def test_sign_in_wrong_user_from_home_page(self):
        user_information = PersonalInformation(email="john@mailinator.com", first_name="John", last_name="Doe",
                                               password="12345")
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.sign_in()
        authentication = Authentication(self.browser)
        authentication.sign_in(user=user_information)
        self.assertTrue(authentication.sign_in_failed())
        account = MyAccount(self.browser)
        name_surname = user_information.first_name + ' ' + user_information.last_name
        self.assertFalse(account.is_user_logged(name_surname))

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
        self.browser.get('http://automationpractice.com/index.php')
        self.assertIn('My Store', self.browser.title)
        home_page = HomePage(self.browser)
        home_page.search_product(product)
        home_page.search_button()
        search_results = SearchPage(self.browser)
        res = search_results.product_found()
        self.assertTrue(res)

    def test_search_existing_product_sign_in_existing_user_and_order(self):
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

    def test_search_existing_product_and_register_user(self):
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
