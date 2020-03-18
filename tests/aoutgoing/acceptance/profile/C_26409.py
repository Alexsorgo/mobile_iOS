from screens.home_screen import HomeScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26409(BaseTest):
    """
    User has the ability to close avatar preview
    """

    def test_c26409(self):
        log.info("Close avatar preview")
        home = HomeScreen(self.driver)
        home.tap_avatar()
        home.close_avatar()

        log.info("Verify Preview was closed")
        Verify.true(home.is_home_screen_displayed(), "Preview was not closed")
