import unittest
from tests_generic.FunctionalTests import FunctionalTests


def suite():
    s = unittest.TestSuite()
    s.addTest(FunctionalTests('test_open_page'))
    s.addTest(FunctionalTests('test_open_shopping_cart_empty_existing_user_not_signed'))
    s.addTest(FunctionalTests('test_open_shopping_cart_empty_existing_user_signed'))
    s.addTest(FunctionalTests('test_product_correctly_inserted_into_cart_user_not_signed_in'))
    s.addTest(FunctionalTests('test_sign_in_existing_user_from_home_page'))
    s.addTest(FunctionalTests('test_sign_in_existing_user_wrong_password_from_home_page'))
    s.addTest(FunctionalTests('test_sign_in_wrong_user_from_home_page'))
    s.addTest(FunctionalTests('test_search_not_existing_product'))
    s.addTest(FunctionalTests('test_search_existing_product'))
    s.addTest(FunctionalTests('test_search_existing_product_sign_in_existing_user_not_tos'))
    s.addTest(FunctionalTests('test_search_existing_product_sign_in_existing_user_and_order'))
    return s


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
