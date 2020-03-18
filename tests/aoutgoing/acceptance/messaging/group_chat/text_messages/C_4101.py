from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.chats.forward_screen import ForwardScreen
from screens.group.group_list_screen import GroupListScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC4101(BaseTest):
    """
    User has the ability to send forward message to group chat
    """
    TEXT_MESSAGE = magic.get_text_message
    FULL_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    GROUP_NAME = config.GROUP_NAME

    def test_c4101(self):
        log.info("Send forward message to group chat")
        menu = Menu(self.driver)
        forward = ForwardScreen(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_forward()
        forward.tap_filter_group()
        forward.select_forward(self.GROUP_NAME)
        forward.tap_send_btn()
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)

        log.info("Verify forward message displayed")
        Verify.true(chat.is_forward_present(self.TEXT_MESSAGE), "No forward message om screen")
