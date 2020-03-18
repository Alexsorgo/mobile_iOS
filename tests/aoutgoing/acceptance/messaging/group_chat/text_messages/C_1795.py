from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC1795(BaseTest):
    """
    User has the ability to delete message for all members from group chat
    """
    GROUP_NAME = config.GROUP_NAME
    DELETE_MESSAGE = magic.get_text_message

    def test_c1795(self):
        log.info("Delete for all message from group chat")
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.DELETE_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.DELETE_MESSAGE)
        chat.tap_context_delete()
        chat.tap_delete_for_all()

        log.info("Verify message deleted")
        Verify.true(chat.is_message_deleted(self.DELETE_MESSAGE), "Message still displayed")
