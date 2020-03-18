import pytest

from configs import config
from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC15486(BaseTest):
    """
    Check context menu items on file message in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c15486(self):
        log.info("heck context menu items on file message")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA, menu.wenums.GALLERY], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_image()
        gallery.open_curtain()
        gallery.tap_send_as_file()
        chat.open_context_menu_last_bubble()

        log.info("Verify context menu items")
        Verify.equals(context_enums.FILE_CONTEXT_MENU_ITEMS, chat.get_context_options(),
                      "Wrong context menu items")
