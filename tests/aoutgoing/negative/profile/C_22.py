from configs import config
from enums import error_enums
from controls.menu import Menu
from screens.profile_edit.my_username_screen import MyUsernameScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC22(BaseTest):
    """
    User has no the ability to edit own Username with min limit chars
    """
    NEW_USERNAME = magic.get_string(1)
    ACTUAL_USERNAME = config.UKRAINE_USERNAME

    def test_c22(self):
        log.info("Edit Username with min char limit")
        profile = MyUsernameScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.EDIT_PROFILE, menu.wenums.MY_USERNAME], menu.wenums.HOME)
        profile.set_username(self.NEW_USERNAME)
        profile.tap_done_btn()

        log.info("Verify alert displayed.")
        Verify.true(profile.error_verify(error_enums.MIN_USERNAME), "The username updated")
