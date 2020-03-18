from configs import config
from screens.chats.chat_screen import ChatScreen
from controls.keyboard_view import KeyboardView
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC19136(BaseTest):

    """
    User has the ability to Choose stickers by tap emoji in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c19136(self):
        log.info("Choose sticker by tap emoji")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        keyboard = KeyboardView(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.open_keyboard()
        keyboard.open_emoji_keyboard()
        keyboard.tap_emoji()

        log.info("Verify sticker preview display")
        result = keyboard.is_sticker_preview_display()
        Verify.true(result, "Sticker preview is not displayed")
