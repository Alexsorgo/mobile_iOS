from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC531(BaseTest):

    """
    User has the ability to delete message only for himself from chat
    """

    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    DELETE_MESSAGE = magic.get_text_message

    def test_c531(self):
        log.info("Delete for all message from p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.DELETE_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.DELETE_MESSAGE)
        chat.tap_context_delete()
        chat.tap_delete_for_both()

        log.info("Verify message deleted")
        Verify.true(chat.is_message_deleted(self.DELETE_MESSAGE), "Message still displayed")
