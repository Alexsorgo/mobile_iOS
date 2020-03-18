from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC28(BaseTest):
    """
    User has the ability to edit message in p2p chat
    """
    TEXT_MESSAGE = magic.get_text_message
    EDIT_MESSAGE = magic.get_text_message
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c28(self):
        log.info("Edit message from p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_edit()
        log.info("Edit message '{}' and set: '{}'".format(self.TEXT_MESSAGE, self.EDIT_MESSAGE))
        chat.set_chat_msg(self.EDIT_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify edited message display")
        Verify.contains(self.EDIT_MESSAGE, chat.get_text_msg(), "No sent message in list")
