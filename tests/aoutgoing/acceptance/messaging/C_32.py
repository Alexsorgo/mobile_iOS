from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC32(BaseTest):
    """
    Nynja User can unblock blocked user
    """
    # TODO: Add one more test for unblock user from chat settings.

    FULL_NAME = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME

    def test_c32(self):
        log.info("Unblock user: '{}'".format(self.FULL_NAME))
        other_profile = OtherProfileScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        Verify.true(chat.unblock_btn(), "User not blocked")
        chat.tap_unblock_btn()
        other_profile.tap_accept_alert()

        log.info("Verify that user unblocked")
        Verify.true(chat.input_present(), "User still blocked")
