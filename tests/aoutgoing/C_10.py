from configs import config
from enums import error_enums
from model.locators import RegistrationPageLocators
from screens.login_screen import LoginScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC10(BaseTest):
    """
    Nynja registration with max limit char in last name
    """
    COUNTRY_CODE_NUMBER = config.CHINA_COUNTRY_CODE
    PHONE_NUMBER = config.CHINA_NUMBER
    FIRST_NAME = config.CHINA_FIRSTNAME
    LAST_NAME = config.INCORRECT_FIRSTNAME

    def test_c10(self):
        login = LoginScreen(self.driver)
        log.info("Registration max limit lastname chars")
        if not self.driver.find_elements(*RegistrationPageLocators.CHECK_PAGE):
            login.set_full_number(self.COUNTRY_CODE_NUMBER, self.PHONE_NUMBER)
            login.tap_confirm_btn()
            login.set_sms()
        login.set_first_name(self.FIRST_NAME)
        login.set_last_name(self.LAST_NAME)
        login.tap_done_btn()

        log.info("Verify user is not registered.")
        Verify.true(login.error_verify(error_enums.MAX_LASTNAME), "Limit doesn't work")
