import pytest

from configs import config
from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC15480(BaseTest):

    """
    Check context menu items on text message in group chat
    """
    GROUP_NAME = config.GROUP_NAME
    TEXT_MESSAGE = magic.get_text_message

    def test_c15480(self):
        log.info("Check context menu items on text message")
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)

        log.info("Verify all context menu items present")
        Verify.equals(context_enums.BASE_CONTEXT_MENU_ITEMS, chat.get_context_options(), "Wrong context menu items")
