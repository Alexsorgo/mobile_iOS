from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.keyboard_view import KeyboardView
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC11247(BaseTest):

    """
    User has the ability to Search stickers by keywords in p2p
    """
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    SEARCH_WORD = "Cool"
    COUNT = 1

    def test_c11247(self):
        log.info("Search stickers by keywords")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        keyboard = KeyboardView(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.tap_sticker_btn()
        keyboard.tap_sticker_search()
        chat.set_chat_msg(self.SEARCH_WORD)
        keyboard.get_sticker_preview_count()

        log.info("Verify sticker preview display")
        Verify.equals(self.COUNT, keyboard.get_sticker_preview_count(), "Sticker preview is not displayed")
