from configs import config
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.profile_edit.my_username_screen import MyUsernameScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify
from utils.helpers.data_generation import magic


class TestC19(BaseTest):
    """
    User has the ability to keep own Username
    """
    NEW_USERNAME = magic.get_username
    ACTUAL_USERNAME = config.CHINA_USERNAME

    def test_c19(self):
        log.info("Keep old Username after update")
        home = HomeScreen(self.driver)
        profile = MyUsernameScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.EDIT_PROFILE, menu.wenums.MY_USERNAME], menu.wenums.CHATS)
        profile.set_username(self.NEW_USERNAME)
        profile.tap_keep_btn()
        home.is_home_screen_displayed()

        log.info("Verify username is not updated")
        Verify.true(home.is_profile_updated(self.ACTUAL_USERNAME), "The username updated")
