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
class TestC15455(BaseTest):
    """
    Check context menu items on media message in p2p chat
    """
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c15455(self):
        log.info("Check context menu items on media message in p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA, menu.wenums.GALLERY], menu.wenums.CHATS)
        menu.tap_first_media()
        chat.open_context_menu_last_bubble()

        log.info("Verify context menu items")
        Verify.equals(context_enums.MEDIA_CONTEXT_MENU_ITEMS, chat.get_context_options(),
                      "Wrong context menu items")
