from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC25385(BaseTest):

    """
    User has the ability to delete message from myself chat
    """
    DELETE_MESSAGE = magic.get_text_message

    def test_c25385(self):
        log.info("Delete message from myself chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.DELETE_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.DELETE_MESSAGE)
        chat.tap_context_delete()
        chat.tap_delete()

        log.info("Verify message deleted")
        Verify.true(chat.is_message_deleted(self.DELETE_MESSAGE), "Message still displayed")
