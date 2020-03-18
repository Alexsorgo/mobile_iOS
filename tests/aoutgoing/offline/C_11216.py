from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC11216(BaseTest):

    """
    User has the ability to send text message in p2p chat with airplane mode
    """
    FRIEND = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME
    TEXT_MESSAGE = magic.get_text_message
    MESSAGE_TYPE = 'text'
    SEND_STATUS = "Delivered"

    def test_c11216(self):
        log.info("Send text message in p2p chat with airplane mode")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify text message sent")
        Verify.contains(self.TEXT_MESSAGE, chat.get_text_msg(), "No sent message in list")

        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.scroll_down_try()

        log.info("Verify message status updated")
        Verify.true(chat.get_send_status(self.MESSAGE_TYPE), "Message status not updated")

