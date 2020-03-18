from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC25772(BaseTest):

    """
    User has the ability to send reply message by sticker in myself chat
    """
    TEXT_MESSAGE = magic.get_text_message
    REPLY_OPTION = context_enums.REPLY

    def test_c25772(self):
        log.info("Send reply message by sticker in myself chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_option(self.REPLY_OPTION)
        chat.tap_sticker_btn()
        chat.send_first_sticker()

        log.info("Verify sticker reply message display")
        Verify.true(chat.is_sticker_reply(), "No sent message in list")
