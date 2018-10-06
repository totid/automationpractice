from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from common.common_classes import PersonalInformation
from common.common_classes import Address


class CreateAccount(BasePage):
    header = 'Create an account'
    first_name = 'customer_firstname'
    last_name = 'customer_lastname'
    password = 'passwd'

    address = 'address1'
    city = 'city'
    state = 'id_state'
    postal_code = 'postcode'
    phone_mobile = 'phone_mobile'

    register_button = 'submitAccount'

    def __init__(self, driver):
        #header_xpath = "//*[contains(text(), " + self.header + ")]"
        header_xpath = "//div[contains(.," + self.header + ")]"
        super().__init__(driver)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, self.first_name))
        )

    def register(self, user_information, address):
        self.driver.find_element_by_id(self.first_name).send_keys(user_information.first_name)
        self.driver.find_element_by_id(self.last_name).send_keys(user_information.last_name)
        self.driver.find_element_by_id(self.password).send_keys(user_information.password)

        self.driver.find_element_by_id(self.address).send_keys(address.address)
        self.driver.find_element_by_id(self.city).send_keys(address.city)

        option_number = '17'
        xpath = "/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[7]/div/select/option[" + option_number + "]"
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, xpath))
        )
        element = self.driver.find_element_by_xpath(xpath)
        element.click()

        self.driver.find_element_by_id(self.postal_code).send_keys(address.postal_code)
        self.driver.find_element_by_id(self.phone_mobile).send_keys(address.phone_mobile)
        self.driver.find_element_by_id(self.register_button).click()