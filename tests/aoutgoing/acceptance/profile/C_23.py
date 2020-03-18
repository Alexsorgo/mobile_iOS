from configs import config
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.profile_edit.my_name_screen import MyNameScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify
from utils.helpers.data_generation import magic


class TestC23(BaseTest):
    """
    User has the ability to edit own first name and last names
    """
    NEW_FIRST_NAME, NEW_LAST_NAME = magic.get_first_and_last_names
    ACTUAL_FIRST_NAME = config.UKRAINE_FIRSTNAME
    ACTUAL_LAST_NAME = config.UKRAINE_LASTNAME

    def test_c23(self):
        log.info("Edit First and Last names")
        menu = Menu(self.driver)
        home = HomeScreen(self.driver)
        profile = MyNameScreen(self.driver)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.EDIT_PROFILE, menu.wenums.MY_NAME], menu.wenums.CHATS)
        profile.set_first_name(self.NEW_FIRST_NAME)
        profile.set_last_name(self.NEW_LAST_NAME)
        profile.tap_done_btn()
        home.is_home_screen_displayed()

        log.info("Verify first and last names are updated successfully.")
        Verify.true(home.is_profile_updated(self.NEW_FIRST_NAME), "The names are not updated")
