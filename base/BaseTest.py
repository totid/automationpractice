import unittest
from selenium import webdriver
from configuration.browser_configuration import CONFIGURATION, CHROME, FIREFOX


class BaseTest(unittest.TestCase):
    driver = None
    browser = None

    def setUp(self):
        self.driver = webdriver
        if CONFIGURATION['browser'] == CHROME:
            self.browser = self.driver.Chrome()
        elif CONFIGURATION['browser'] == FIREFOX:
            self.browser = self.driver.Firefox()
        else:
            raise Exception('Browser not supported')
        self.browser.delete_all_cookies()

    def tearDown(self):
        self.browser.quit()

