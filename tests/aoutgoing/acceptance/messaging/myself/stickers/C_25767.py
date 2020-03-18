from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25767(BaseTest):
    """
    User has the ability to open stickers board
    """

    def test_c25767(self):
        log.info("Open stickers board")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.tap_sticker_btn()

        log.info("Verify sticker board open")
        Verify.true(chat.is_sticker_board_display(), "No sticker board")
