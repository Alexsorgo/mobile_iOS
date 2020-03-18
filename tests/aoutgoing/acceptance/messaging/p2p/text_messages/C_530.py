from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC530(BaseTest):

    """
    User has the ability to send link message in p2p chat
    """
    PHONE_NUMBER_MESSAGE = magic.get_phone_number
    EMAIL_MESSAGE = magic.get_email
    URL_MESSAGE = magic.get_url
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c530(self):
        log.info("Send link message in p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
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
