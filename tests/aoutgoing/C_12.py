from configs import config
from model.locators import RegistrationPageLocators
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.manage_users import Manager
from utils.logs import log
from utils.verify import Verify


class TestC12(BaseTest):
    """
    Nynja registration
    """
    COUNTRY_CODE_NUMBER = config.CHINA_COUNTRY_CODE
    PHONE_NUMBER = config.CHINA_NUMBER
    FIRST_NAME = config.CHINA_FIRSTNAME
    LAST_NAME = config.CHINA_LASTNAME

    def test_c12(self):
        login = LoginScreen(self.driver)
        home = HomeScreen(self.driver)
        log.info("Registration with valid data: '{}'".format(self.PHONE_NUMBER))
        if not self.driver.find_elements(*RegistrationPageLocators.CHECK_PAGE):
            login.set_full_number(self.COUNTRY_CODE_NUMBER, self.PHONE_NUMBER)
            login.tap_confirm_btn()
            login.set_sms()
        login.set_first_name(self.FIRST_NAME)
        login.set_last_name(self.LAST_NAME)
        login.tap_done_btn()

        log.info("Verify user is registered successfully.")
        Verify.true(home.is_home_screen_displayed(), "Home Screen is not displayed")

        manage = Manager(self.driver)
        manage.log_out()
