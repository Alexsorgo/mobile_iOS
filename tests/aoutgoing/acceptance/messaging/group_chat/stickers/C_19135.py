from configs import config
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC19135(BaseTest):

    """
    User has the ability to send sticker message in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c19135(self):
        log.info("Send sticker message in group chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.tap_sticker_btn()
        chat.send_first_sticker()

        log.info("Verify sticker message display")
        Verify.true(chat.is_sticker_displayed(), "No sent message in list")
