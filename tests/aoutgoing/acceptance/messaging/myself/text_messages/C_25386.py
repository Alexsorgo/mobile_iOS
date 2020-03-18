from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC25386(BaseTest):

    """
    User has the ability to send link message in myself chat
    """
    PHONE_NUMBER_MESSAGE = magic.get_phone_number
    EMAIL_MESSAGE = magic.get_email
    URL_MESSAGE = magic.get_url

    def test_c25386(self):
        log.info("Send link message in myself chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.PHONE_NUMBER_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.PHONE_NUMBER_MESSAGE)

        log.info("Verify phone number looks like link")
        Verify.true(chat.is_link(), "Message not a link")
        chat.close_context()

        chat.set_chat_msg(self.EMAIL_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.EMAIL_MESSAGE)

        log.info("Verify email looks like link")
        Verify.true(chat.is_link(), "Message not a link")
        chat.close_context()

        chat.set_chat_msg(self.URL_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.URL_MESSAGE)

        log.info("Verify url looks like link")
        Verify.true(chat.is_link(), "Message not a link")
