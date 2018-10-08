from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Authentication(BasePage):
    header = 'Authentication'
    email_create = 'email_create'
    email_create_button = 'SubmitCreate'

    email_existing = 'email'
    passwd_existing = 'passwd'
    sign_in_button = 'SubmitLogin'
    alert = 'alert-danger'

    def __init__(self, driver):
        header_xpath = "//*[contains(text(), " + self.header.upper() + ")]"
        super().__init__(driver)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, header_xpath))
        )

    def create_an_account(self, email):
        self.driver.find_element_by_id(self.email_create).send_keys(email)
        self.driver.find_element_by_id(self.email_create_button).click()

    def sign_in(self, user):
        self.driver.find_element_by_id(self.email_existing).send_keys(user.email)
        self.driver.find_element_by_id(self.passwd_existing).send_keys(user.password)
        self.driver.find_element_by_id(self.sign_in_button).click()

    def sign_in_failed(self):
        try:
            self.driver.find_element_by_class_name(self.alert)
        except NoSuchElementException:
            return False
        return True
