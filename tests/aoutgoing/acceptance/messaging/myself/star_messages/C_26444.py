from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26444(BaseTest):
    """
    User has the ability unstar text message from myself chat and check Home screen
    """

    STARED_MESSAGE = magic.get_text_message

    def test_c26444(self):
        log.info("Unstar message: '{}'".format(self.STARED_MESSAGE))
        main = HomeScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_option(context_enums.STAR)
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_option(context_enums.UNSTAR)
        menu.long_press_wheel()

        log.info("Verify stared message doesn't display on home screen")
        Verify.false(main.is_starred_displayed(self.STARED_MESSAGE), "Starred message still displayed")
