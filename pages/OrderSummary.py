from base.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class OrderSummary(BasePage):
    header = 'Order summary'
    confirm = 'button-medium'
    confirm_xpath = '/html/body/div/div[2]/div/div[3]/div/form/p/button'

    def confirm(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.confirm_xpath))
        )
        confirm_button = self.driver.find_element_by_xpath(self.confirm_xpath)
        confirm_button.click()

