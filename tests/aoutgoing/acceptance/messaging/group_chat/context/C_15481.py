import pytest

from configs import config
from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC15481(BaseTest):
    """
    Check context menu items on translated message in group chat
    """

    MESSAGE = 'Двери'
    TRANSLATED_MESSAGE = 'Doors'
    GROUP_NAME = config.GROUP_NAME

    def test_c15481(self):
        log.info("Check context menu items on translated message")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.MESSAGE)
        chat.tap_context_translate()
        chat.open_translation_context_menu()

        log.info("Verify context menu items")
        Verify.equals(context_enums.TRANSLATED_CONTEXT_MENU_ITEMS,chat.get_context_options(),
                      "Wrong context menu items")
