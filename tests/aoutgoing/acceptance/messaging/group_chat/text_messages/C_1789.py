from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC1789(BaseTest):
    """
    User has the ability to delete message only for himself from group chat
    """
    GROUP_NAME = config.GROUP_NAME
    DELETE_MESSAGE = config.DELETE_MESSAGE

    def test_c1789(self):
        log.info("Delete message from group chat")
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.DELETE_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.DELETE_MESSAGE)
        chat.tap_context_delete()
        chat.tap_delete_for_me()

        log.info("Verify message deleted")
        Verify.true(chat.is_message_deleted(self.DELETE_MESSAGE), "Message still displayed")
