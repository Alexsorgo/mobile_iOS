from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2031(BaseTest):
    """
    User has the ability to see that translated message was edited
    """

    MESSAGE = 'Руки'
    EDIT_MESSAGE = magic.get_text_message
    TRANSLATED_MESSAGE = 'Arms'
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c2031(self):
        log.info("Edit '{}' message and check outdated label".format(self.MESSAGE))
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.MESSAGE)
        chat.tap_context_translate()
        chat.open_context_menu(self.MESSAGE)
        chat.tap_context_edit()
        chat.set_chat_msg(self.EDIT_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify translated message is outdated")
        Verify.true(chat.is_outdated(), "Outdated label doesn't displayed")
