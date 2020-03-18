from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26445(BaseTest):
    """
    User has the ability unstar text message from starred screen
    """

    STARED_MESSAGE = magic.get_text_message

    def test_c26445(self):
        log.info("Unstar message: '{}'".format(self.STARED_MESSAGE))
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_option(context_enums.STAR)
        chat.stared_present()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_option(context_enums.UNSTAR)

        log.info("Verify stared message doesn't display on home screen")
        Verify.false(chat.stared_present(), "Starred message still displayed")
