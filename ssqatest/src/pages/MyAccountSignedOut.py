from ssqatest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator  # import class from
# module (first instance is module, second instance is class

from ssqatest.src.helpers.config_helpers import get_base_url
from ssqatest.src.Selenium_Extended import Selenium_Extended
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):
    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = Selenium_Extended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()  # reduces repeatability using function from helpers file
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to {my_account_url}")

        self.driver.get(my_account_url)
        # self.driver.get('http://demostore.supersqa.com/my-account/')

    def input_login_username(self, username):
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(self.LOGIN_USER_NAME)
        # ).send_keys(username)

        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)  # This line does the same thing as the above 3
        # using "selenium extended" class

    def input_login_password(self, password):
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(self.LOGIN_PASSWORD)
        # ).send_keys(password)

        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(self.LOGIN_BUTTON)
        # ).click()

        logger.debug("Clicking 'login' button.")
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)  # Same as input_login_username but
        # with different locators

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)  # Same as input_login_username but
        # with different locators

    def click_register_button(self):
        logger.debug("Clicking 'Register' button.")
        self.sl.wait_and_click(self.REGISTER_BUTTON)
