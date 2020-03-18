from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC1788(BaseTest):
    """
    User has the ability to send voice message in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c1788(self):
        log.info("Send voice message in group chat")
        chat = ChatScreen(self.driver)
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.record_voice_msg()
        chat.tap_record_send()

        log.info("Verify voice message sent.")
        Verify.true(chat.is_voice_displayed(), "No sent voice message in list")
