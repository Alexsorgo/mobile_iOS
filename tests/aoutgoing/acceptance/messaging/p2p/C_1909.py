from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC1909(BaseTest):
    """
    User has the ability to reply text message in p2p chat
    """

    TEXT_MESSAGE = magic.get_text_message
    REPLY_MESSAGE = magic.get_text_message
    FULL_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c1909(self):
        log.info("Send and reply message in p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_reply()
        chat.set_chat_msg(self.REPLY_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify text message replied.")
        Verify.true(chat.is_replay_displayed(self.REPLY_MESSAGE, self.TEXT_MESSAGE), "No replied message in list")
