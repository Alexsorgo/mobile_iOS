from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC534(BaseTest):
    """
    User has the ability to send voice message in myself chat
    """

    def test_c534(self):
        log.info("Send message in myself")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.record_voice_msg()
        chat.tap_record_send()

        log.info("Verify voice message sent.")
        Verify.true(chat.is_voice_displayed(), "No sent voice message in list")
