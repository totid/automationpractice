from base.BasePage import BasePage


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

