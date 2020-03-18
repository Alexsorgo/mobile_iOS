from configs import config
from enums import context_enums
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC11224(BaseTest):

    """
    User has the ability to delete message only for himself from p2p chat with airplane mode
    """
    FRIEND = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME
    DELETE_MESSAGE = magic.get_text_message
    CONTEXT_OPTION = context_enums.DELETE

    def test_c11224(self):
        log.info("Delete message from p2p chat with airplane mode")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.set_chat_msg(self.DELETE_MESSAGE)
        chat.tap_send_btn()
        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.open_context_menu(self.DELETE_MESSAGE)
        chat.tap_context_option(self.CONTEXT_OPTION)
        chat.tap_delete_for_me()
        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.scroll_down_try()

        log.info("Verify message deleted")
        Verify.true(chat.is_message_deleted(self.DELETE_MESSAGE), "Message still displayed")
