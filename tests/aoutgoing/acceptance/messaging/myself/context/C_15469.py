import pytest

from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC15469(BaseTest):

    """
    Check context menu items on sticker message in myself chat
    """

    def test_c15469(self):
        log.info("Check context menu items on sticker message")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.tap_sticker_btn()
        chat.send_first_sticker()
        chat.open_sticker_context_menu()

        log.info("Verify sticker message context menu items")
        Verify.equals(context_enums.STICKERS_CONTEXT_MENU_ITEMS, chat.get_context_options(), "Items not identical")
