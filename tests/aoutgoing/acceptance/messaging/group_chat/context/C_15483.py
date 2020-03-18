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
class TestC15483(BaseTest):
    """
    Check context menu items on voice message in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c15483(self):
        log.info("Check context menu items on voice message")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.record_voice_msg()
        chat.tap_record_send()
        chat.open_context_menu_last_bubble()

        log.info("Verify context menu items")
        Verify.equals(context_enums.VOICE_CONTEXT_MENU_ITEMS, chat.get_context_options(),
                      "Wrong context menu items")
