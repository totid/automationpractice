from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class CartPopupPage(BasePage):
    name = 'clearfix'
    proceed_to_checkout_button = '/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a'

    def __init__(self, driver):
        super().__init__(driver)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, self.name))
        )

    def proceed_to_checkout(self):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.proceed_to_checkout_button))
        )
        checkout_button = self.driver.find_element_by_xpath(self.proceed_to_checkout_button)
        checkout_button.click()
