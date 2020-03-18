from screens.chats.chat_screen import ChatScreen
from controls.keyboard_view import KeyboardView
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25771(BaseTest):

    """
    User has the ability to Search stickers by emoji in myself
    """
    COUNT = 1

    def test_c25771(self):
        log.info("Search stickers by emoji")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        keyboard = KeyboardView(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.tap_sticker_btn()
        keyboard.tap_sticker_search()
        keyboard.open_emoji_keyboard()
        keyboard.tap_emoji()

        log.info("Verify sticker search display")
        Verify.equals(self.COUNT, keyboard.get_sticker_preview_count(), "No stickers in the search")
