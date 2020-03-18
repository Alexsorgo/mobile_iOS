from configs import config
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC19133(BaseTest):
    """
    User has the ability to open stickers board
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c19133(self):
        log.info("Open stickers board")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.tap_sticker_btn()

        log.info("Verify sticker board open")
        Verify.true(chat.is_sticker_board_display(), "No sticker board")
