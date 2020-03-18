from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.keyboard_view import KeyboardView
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC11248(BaseTest):

    """
    User has the ability to Search stickers by emoji in p2p
    """
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    COUNT = 1

    def test_c11248(self):
        log.info("Search stickers by emoji")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        keyboard = KeyboardView(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.tap_sticker_btn()
        keyboard.tap_sticker_search()
        keyboard.open_emoji_keyboard()
        keyboard.tap_emoji()

        log.info("Verify sticker search display")
        Verify.equals(self.COUNT, keyboard.get_sticker_preview_count(), "No stickers in the search")
