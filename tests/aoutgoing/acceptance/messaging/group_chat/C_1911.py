from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC1911(BaseTest):
    """
    User has the ability open reply screen from group chat
    """

    TEXT_MESSAGE = magic.get_text_message
    REPLY_MESSAGE = magic.get_text_message
    GROUP_NAME = config.GROUP_NAME
    REPLY_COUNT = '1'

    def test_c1911(self):
        log.info("Open replied screen from first replied msg in group chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.open_replay(self.REPLY_COUNT)

        log.info("Verify replied screen open")
        Verify.true(chat.is_replay_screen(), "Replied screen doesn't display")
