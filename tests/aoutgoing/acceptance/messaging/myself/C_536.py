from screens.chats.chat_screen import ChatScreen
from screens.chats.location_screen import LocationScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC536(BaseTest):
    """
    User has the ability to send location message in myself chat
    """

    def test_c536(self):
        log.info("Send location message")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        location = LocationScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.LOCATION], menu.wenums.CHATS)
        location.tap_send_location()

        log.info("Verify location message sent.")
        Verify.true(chat.is_location_displayed(), "No sent message in list")
