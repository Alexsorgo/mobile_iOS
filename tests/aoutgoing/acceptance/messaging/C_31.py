from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC31(BaseTest):
    """
    Nynja User can block another user
    """

    FULL_NAME = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME

    def test_c31(self):
        log.info("Block user: '{}'".format(self.FULL_NAME))
        menu = Menu(self.driver)
        other_profile = OtherProfileScreen(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        chat.tap_open_profile()
        other_profile.tap_block_user()
        other_profile.tap_accept_alert()
        other_profile.tap_send_message()

        log.info("Verify that user blocked")
        Verify.true(chat.unblock_btn(), "User not blocked")
