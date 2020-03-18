from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC532(BaseTest):
    """
    User has the ability to send text message in myself chat
    """
    TEXT_MESSAGE = magic.get_text_message

    def test_c532(self):
        log.info("Send message in myself")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify text message sent.")
        Verify.contains(self.TEXT_MESSAGE, chat.get_text_msg(), "No sent message in list")
