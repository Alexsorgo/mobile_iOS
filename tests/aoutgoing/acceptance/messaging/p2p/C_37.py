from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.chats.location_screen import LocationScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC37(BaseTest):
    """
    User has the ability to send location message in p2p chat
    """

    FULL_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c37(self):
        log.info("Send location message in p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        location = LocationScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.LOCATION], menu.wenums.CHATS)
        location.tap_send_location()

        log.info("Verify location message sent.")
        Verify.true(chat.is_location_displayed(), "No sent message in list")
