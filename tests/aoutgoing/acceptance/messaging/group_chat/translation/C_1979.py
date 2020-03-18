from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC1979(BaseTest):
    """
    User has the ability translate aoutgoing message in group chat
    """

    MESSAGE = 'Привет'
    TRANSLATED_MESSAGE = 'Hello'
    GROUP_NAME = config.GROUP_NAME

    def test_c1979(self):
        log.info("Translate message: '{}'".format(self.MESSAGE))
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.MESSAGE)
        chat.tap_context_translate()

        log.info("Verify message translated")
        expected = [self.MESSAGE, self.TRANSLATED_MESSAGE]
        actual = chat.get_translated_msg()
        Verify.equals(expected, actual, "No translated messages on screen")
