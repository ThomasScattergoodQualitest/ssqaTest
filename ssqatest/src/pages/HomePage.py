from ssqatest.src.helpers.config_helpers import get_base_url
from ssqatest.src.Selenium_Extended import Selenium_Extended
from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators


class HomePage(HomePageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = Selenium_Extended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BUTTON)
