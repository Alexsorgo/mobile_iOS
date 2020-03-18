from configs import config
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC13(BaseTest):
    """
    Nynja first run and login
    """

    PHONE_NUMBER = config.CHINA_NUMBER
    COUNTRY_CODE = config.CHINA_COUNTRY_CODE

    def test_c13(self):
        log.info("Login to Nynja APP, set phone number '{}'".format(self.PHONE_NUMBER))

        login = LoginScreen(self.driver)
        home = HomeScreen(self.driver)
        login.set_full_number(self.COUNTRY_CODE, self.PHONE_NUMBER)
        login.tap_confirm_btn()
        login.set_sms()

        log.info("Verify user is authorized successfully.")
        Verify.true(home.is_home_screen_displayed(), "Home Screen is not displayed")
