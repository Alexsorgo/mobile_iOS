from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC4105(BaseTest):
    """
    User has the ability reply for a message by voice message in p2p chat
    """

    TEXT_MESSAGE = magic.get_text_message
    FULL_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c4105(self):
        log.info("Reply for a message by voice message in p2p chat ")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_reply()
        chat.record_voice_msg()
        chat.tap_record_send()

        log.info("Verify reply voice message displayed")
        Verify.true(chat.is_voice_reply(self.TEXT_MESSAGE), "No replied voice message")
