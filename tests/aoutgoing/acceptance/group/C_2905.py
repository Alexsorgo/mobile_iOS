from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from screens.group.group_options_screen import GroupOptionScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2905(BaseTest):
    """
    User has the ability to clear group chat history
    """
    MESSAGE = magic.get_text_message

    def test_c2905(self):
        log.info("Clear group chat history")
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        chat = ChatScreen(self.driver)
        options = GroupOptionScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_first_group()
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()
        chat.tap_open_profile()
        options.clear_history()
        options.back_to_chat()

        log.info("Verify group chat history cleared")
        Verify.true(chat.is_history_removed(), "System message does't displayed or text message present")
