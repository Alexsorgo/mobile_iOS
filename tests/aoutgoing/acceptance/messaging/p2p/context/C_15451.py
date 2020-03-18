import pytest

from configs import config
from enums import context_enums
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC15451(BaseTest):
    """
    Check context menu items on translated message in p2p chat
    """

    MESSAGE = 'Двери'
    TRANSLATED_MESSAGE = 'Doors'
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c15451(self):
        log.info("Check context menu items on translated message")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.MESSAGE)
        chat.tap_context_translate()
        chat.open_translation_context_menu()

        log.info("Verify context menu items")
        Verify.equals(context_enums.TRANSLATED_CONTEXT_MENU_ITEMS, chat.get_context_options(),
                      "Wrong context menu items")
