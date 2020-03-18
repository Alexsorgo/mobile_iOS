from configs import config
from enums import error_enums
from screens.login_screen import LoginScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC07(BaseTest):
    """
    Nynja first run and login with not allowed phone number
    """

    PHONE_NUMBER = config.NOTALLOWED_LOGIN
    COUNTRY_CODE = config.AMERICA_COUNTRY_CODE

    def test_c07(self):
        log.info("Login to Nynja APP, set phone number '{}'".format(self.PHONE_NUMBER))
        login = LoginScreen(self.driver)
        login.set_full_number(self.COUNTRY_CODE, self.PHONE_NUMBER)
        login.tap_confirm_btn()

        log.info("Verify user is unauthorized.")
        Verify.true(login.error_verify(error_enums.NOT_ALLOW_NUMBER),
                    "Alert doesn't displayed")
