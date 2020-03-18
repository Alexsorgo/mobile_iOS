from screens.chats.chat_screen import ChatScreen
from controls.keyboard_view import KeyboardView
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25770(BaseTest):

    """
    User has the ability to Search stickers by keywords in myself
    """
    SEARCH_WORD = "Cool"
    COUNT = 1

    def test_c25770(self):
        log.info("Search stickers by keywords")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        keyboard = KeyboardView(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.tap_sticker_btn()
        keyboard.tap_sticker_search()
        chat.set_chat_msg(self.SEARCH_WORD)
        keyboard.get_sticker_preview_count()

        log.info("Verify sticker preview display")
        Verify.equals(self.COUNT, keyboard.get_sticker_preview_count(), "Sticker preview is not displayed")
