from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.server.messaging.server_send_message import incoming_message
from utils.verify import Verify


class TestC43774(BaseTest):
    """
    User has the ability to received location message from p2p chat
    """
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    CHAT_TYPE = 'p2p'
    MIME = 'location'

    def test_c43774(self):
        log.info("Received location message from p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        incoming_message(self.CHAT_TYPE, self.MIME)

        log.info("Verify location message received.")
        Verify.true(chat.is_received_location_displayed(), "No received location message in list")
