from configs import config
from enums import error_enums
from model.locators import RegistrationPageLocators
from screens.login_screen import LoginScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC11(BaseTest):
    """
    Nynja registration with empty first name
    """
    COUNTRY_CODE_NUMBER = config.CHINA_COUNTRY_CODE
    PHONE_NUMBER = config.CHINA_NUMBER
    FIRST_NAME = ''
    LAST_NAME = config.CHINA_LASTNAME

    def test_c11(self):
        login = LoginScreen(self.driver)
        log.info("Registration empty first name")
        if not self.driver.find_elements(*RegistrationPageLocators.CHECK_PAGE):
            login.set_full_number(self.COUNTRY_CODE_NUMBER, self.PHONE_NUMBER)
            login.tap_confirm_btn()
            login.set_sms()
        login.set_first_name(self.FIRST_NAME)
        login.set_last_name(self.LAST_NAME)
        login.tap_done_btn()

        log.info("Verify user is not registered.")
        Verify.true(login.error_verify(error_enums.FIRSTNAME_REQUIRED), "First Name field not required")
