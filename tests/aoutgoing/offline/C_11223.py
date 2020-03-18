from configs import config
from enums import context_enums
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC11223(BaseTest):

    """
    User has the ability to edit message in p2p chat with airplane mode
    """
    FRIEND = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME
    TEXT_MESSAGE = magic.get_text_message
    EDIT_MESSAGE = magic.get_text_message
    CONTEXT_OPTION = context_enums.EDIT
    MESSAGE_TYPE = 'text'

    def test_c11223(self):
        log.info("Edit message from p2p chat with airplane mode")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_option(self.CONTEXT_OPTION)
        log.info("Edit message '{}' and set: '{}'".format(self.TEXT_MESSAGE, self.EDIT_MESSAGE))
        chat.set_chat_msg(self.EDIT_MESSAGE)
        chat.tap_send_btn()
        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.scroll_down_try()

        log.info("Verify edited message display")
        Verify.contains(self.EDIT_MESSAGE, chat.get_text_msg(), "No sent message in list")

        log.info("Verify message status updated")
        Verify.true(chat.get_send_status(self.MESSAGE_TYPE), "Message status not updated")
