from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC1978(BaseTest):
    """
    User has the ability translate aoutgoing message in p2p chat
    """

    MESSAGE = 'Привет'
    TRANSLATED_MESSAGE = 'Hello'
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c1978(self):
        log.info("Translate message: '{}'".format(self.MESSAGE))
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.MESSAGE)
        chat.tap_context_translate()

        log.info("Verify message translated")
        expected = [self.MESSAGE, self.TRANSLATED_MESSAGE]
        actual = chat.get_translated_msg()
        Verify.equals(expected, actual, "No translated messages on screen")
