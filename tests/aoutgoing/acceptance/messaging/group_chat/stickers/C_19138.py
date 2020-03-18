from configs import config
from screens.chats.chat_screen import ChatScreen
from controls.keyboard_view import KeyboardView
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC19138(BaseTest):

    """
    User has the ability to Search stickers by emoji in group
    """
    GROUP_NAME = config.GROUP_NAME
    COUNT = 1

    def test_c19138(self):
        log.info("Search stickers by emoji")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        keyboard = KeyboardView(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.tap_sticker_btn()
        keyboard.tap_sticker_search()
        keyboard.open_emoji_keyboard()
        keyboard.tap_emoji()

        log.info("Verify sticker search display")
        Verify.equals(self.COUNT, keyboard.get_sticker_preview_count(), "No stickers in the search")
