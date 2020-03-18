from selenium.webdriver.common.by import By

from configs import config
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.profile_edit.my_username_screen import MyUsernameScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify
from utils.helpers.data_generation import magic


class TestC20(BaseTest):
    """
    User has the ability to edit own Username
    """
    EDIT_USERNAME = magic.get_username
    OLD_USERNAME = config.CHINA_USERNAME

    def test_c20(self):
        log.info("Edit Username")
        home = HomeScreen(self.driver)
        profile = MyUsernameScreen(self.driver)
        menu = Menu(self.driver)
        self.driver.find_element(*(By.ID, self.OLD_USERNAME))
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.EDIT_PROFILE, menu.wenums.MY_USERNAME], menu.wenums.CHATS)
        profile.set_username(self.EDIT_USERNAME)
        profile.tap_done_btn()
        home.is_home_screen_displayed()

        log.info("Verify username is updated successfully.")
        Verify.true(home.is_profile_updated(self.EDIT_USERNAME), "The names are not updated")
