from enums import error_enums
from controls.menu import Menu
from screens.profile_edit.my_name_screen import MyNameScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify
from utils.helpers.data_generation import magic


class TestC24(BaseTest):
    """
    User has no the ability to edit empty first name
    """
    NEW, NEW_LAST_NAME = magic.get_first_and_last_names
    NEW_FIRST_NAME = ''

    def test_c24(self):
        log.info("Edit First and Last names with empty First name")
        profile = MyNameScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.EDIT_PROFILE, menu.wenums.MY_NAME], menu.wenums.HOME)
        profile.set_first_name(self.NEW_FIRST_NAME)
        profile.set_last_name(self.NEW_LAST_NAME)
        profile.tap_done_btn()

        log.info("Verify first name field required.")
        Verify.true(profile.error_verify(error_enums.FIRSTNAME_REQUIRED), "The names updated")
