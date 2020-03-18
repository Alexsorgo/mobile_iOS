import pytest

from configs import config
from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from screens.chats.location_screen import LocationScreen
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC15487(BaseTest):
    """
    Check context menu items on location message in group chat
    """

    GROUP_NAME = config.GROUP_NAME

    def test_c15487(self):
        log.info("Check context menu items on location message")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        location = LocationScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.LOCATION, menu.wenums.SEND_LOCATION], menu.wenums.CHATS)
        location.tap_send_location()
        chat.open_context_menu_last_bubble()

        log.info("Verify context menu items")
        Verify.equals(context_enums.LOCATION_CONTEXT_MENU_ITEMS, chat.get_context_options(),
                      "Wrong context menu items")
