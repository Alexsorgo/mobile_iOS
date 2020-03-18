from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC1908(BaseTest):
    """
    User has the ability to reply text message in group chat
    """

    GROUP_NAME = config.GROUP_NAME
    TEXT_MESSAGE = magic.get_text_message
    REPLY_MESSAGE = magic.get_text_message

    def test_c1908(self):
        log.info("Send and reply message in group chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_reply()
        chat.set_chat_msg(self.REPLY_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify text message replied.")
        Verify.true(chat.is_replay_displayed(self.TEXT_MESSAGE, self.REPLY_MESSAGE), "No replied message in list")
