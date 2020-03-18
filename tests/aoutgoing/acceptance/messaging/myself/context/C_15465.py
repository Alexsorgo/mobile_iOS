import pytest

from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC15465(BaseTest):

    """
    Check context menu items on text message in myself chat
    """
    TEXT_MESSAGE = magic.get_text_message

    def test_c15465(self):
        log.info("Check context menu items on text message")
        chat = ChatScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)

        log.info("Verify all context menu items present")
        Verify.equals(context_enums.BASE_CONTEXT_MENU_ITEMS, chat.get_context_options(), "Wrong context menu items")
