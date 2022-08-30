from ssqatest.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from ssqatest.src.Selenium_Extended import Selenium_Extended

class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = Selenium_Extended(self.driver)

    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)