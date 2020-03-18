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
class TestC15454(BaseTest):

    """
    Check context menu items on sticker message in p2p chat
    """
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c15454(self):
        log.info("Check context menu items on sticker message")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.tap_sticker_btn()
        chat.send_first_sticker()
        chat.open_sticker_context_menu()

        log.info("Verify sticker message context menu items")
        Verify.equals(context_enums.STICKERS_CONTEXT_MENU_ITEMS, chat.get_context_options(), "Items not identical")
