from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class MyAccount(BasePage):
    history = ''
    order_slips = ''
    addresses = ''
    identity = ''
    wishlist = ''

    header = 'My account'
