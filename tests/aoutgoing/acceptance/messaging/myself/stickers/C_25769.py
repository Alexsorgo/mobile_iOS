from screens.chats.chat_screen import ChatScreen
from controls.keyboard_view import KeyboardView
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25769(BaseTest):

    """
    User has the ability to Choose stickers by tap emoji in myself
    """

    def test_c25769(self):
        log.info("Choose sticker by tap emoji")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        keyboard = KeyboardView(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.open_keyboard()
        keyboard.open_emoji_keyboard()
        keyboard.tap_emoji()

        log.info("Verify sticker preview display")
        result = keyboard.is_sticker_preview_display()
        Verify.true(result, "Sticker preview is not displayed")
