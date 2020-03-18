from configs import config
from enums import context_enums
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC7367(BaseTest):
    """
    User has the ability unstar text message from starred screen
    """

    STARED_MESSAGE = magic.get_text_message
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c7367(self):
        log.info("Unstar message: '{}'".format(self.STARED_MESSAGE))
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_option(context_enums.STAR)
        chat.stared_present()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_option(context_enums.UNSTAR)

        log.info("Verify stared message doesn't display on home screen")
        Verify.false(chat.stared_present(), "Starred message still displayed")
