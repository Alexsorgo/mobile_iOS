from configs import config
from screens.chats.chat_screen import ChatScreen
from controls.keyboard_view import KeyboardView
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC19137(BaseTest):

    """
    User has the ability to Search stickers by keywords in group chat
    """
    GROUP_NAME = config.GROUP_NAME
    SEARCH_WORD = "Cool"
    COUNT = 1

    def test_c19137(self):
        log.info("Search stickers by keywords")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        keyboard = KeyboardView(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.tap_sticker_btn()
        keyboard.tap_sticker_search()
        chat.set_chat_msg(self.SEARCH_WORD)

        log.info("Verify sticker preview display")
        Verify.equals(self.COUNT, keyboard.get_sticker_preview_count(), "Sticker preview is not displayed")
