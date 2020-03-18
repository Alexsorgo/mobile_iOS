from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC1786(BaseTest):
    """
    User has the ability to send text message in group chat
    """
    GROUP_NAME = config.GROUP_NAME
    TEXT_MESSAGE = magic.get_text_message

    def test_c1786(self):
        log.info("Send text message in group chat")
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify text message sent.")
        Verify.contains(self.TEXT_MESSAGE, chat.get_text_msg(), "No sent message in list")
