from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.server.messaging.server_send_message import incoming_message
from utils.verify import Verify


class TestC43772(BaseTest):
    """
    User has the ability to received text message from p2p chat
    """
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    CHAT_TYPE = 'p2p'
    MIME = 'text'
    TEXT_MESSAGE = magic.get_text_message

    def test_c43772(self):
        log.info("Received text message from p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        incoming_message(self.CHAT_TYPE, self.MIME, message_text=self.TEXT_MESSAGE)

        log.info("Verify text message received.")
        Verify.contains(self.TEXT_MESSAGE, chat.get_received_text_msg(), "No received text message in list")
