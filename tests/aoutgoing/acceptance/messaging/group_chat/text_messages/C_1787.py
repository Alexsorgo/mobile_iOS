from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC1787(BaseTest):
    """
    User has the ability to edit message in group chat
    """
    GROUP_NAME = config.GROUP_NAME
    TEXT_MESSAGE = magic.get_text_message
    EDIT_MESSAGE = magic.get_text_message

    def test_c1787(self):
        log.info("Edit message '{}' and set: '{}' in group chat".format(self.TEXT_MESSAGE, self.EDIT_MESSAGE))
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_edit()
        chat.set_chat_msg(self.EDIT_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify edited message display")
        Verify.contains(self.EDIT_MESSAGE, chat.get_text_msg(), "No sent message in list")
