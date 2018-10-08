from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class MyAccount(BasePage):
    history = ''
    order_slips = ''
    addresses = ''
    identity = ''
    wishlist = ''

    header = 'My account'

    def is_user_logged(self, user):
        logged_user = self.driver.find_elements_by_tag_name("span")[0].text
        if logged_user == user:
            return True
        else:
            return False

