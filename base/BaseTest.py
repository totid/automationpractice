import unittest
from selenium import webdriver


class BaseTest(unittest.TestCase):
    driver = None
    browser = None

    def setUp(self):
        self.driver = webdriver
        self.browser = self.driver.Firefox()

    def tearDown(self):
        self.browser.quit()

