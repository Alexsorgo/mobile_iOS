from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC1910(BaseTest):
    """
    User has the ability to open reply screen from p2p chat
    """

    TEXT_MESSAGE = magic.get_text_message
    REPLY_MESSAGE = magic.get_text_message
    FULL_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    # TODO: Make correct locator
    REPLY_COUNT = '1'

    def test_c1910(self):
        log.info("Open reply screen for replied msg in p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        chat.open_replay(self.REPLY_COUNT)

        log.info("Verify reply screen open")
        Verify.true(chat.is_replay_screen(), "Reply screen doesn't display")
