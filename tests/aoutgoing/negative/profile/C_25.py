from enums import error_enums
from controls.menu import Menu
from screens.profile_edit.my_name_screen import MyNameScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify
from utils.helpers.data_generation import magic


class TestC25(BaseTest):
    """
    User has no the ability to edit own first name with max limit chars
    """
    NEW, NEW_LAST_NAME = magic.get_first_and_last_names
    NEW_FIRST_NAME = magic.get_string(33)

    def test_c25(self):
        log.info("Edit First and Last names with first name max char limit")
        profile = MyNameScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.EDIT_PROFILE, menu.wenums.MY_NAME], menu.wenums.HOME)
        profile.set_first_name(self.NEW_FIRST_NAME)
        profile.set_last_name(self.NEW_LAST_NAME)
        profile.tap_done_btn()

        log.info("Verify alert displayed")
        Verify.true(profile.error_verify(error_enums.MAX_FIRSTNAME), "The names updated")
