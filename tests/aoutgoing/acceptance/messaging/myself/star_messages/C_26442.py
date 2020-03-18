from configs import config
from screens.chats.chat_screen import ChatScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26442(BaseTest):
    """
    User has the ability star message from myself chat
    """
    STARED_MESSAGE = magic.get_text_message

    def test_c26442(self):
        log.info("Star message: '{}'".format(config.STARED_MESSAGE))
        main = HomeScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_star()
        menu.long_press_wheel()
        main.tap_stared_msg(self.STARED_MESSAGE)

        log.info("Verify that message stared")
        Verify.true(chat.stared_present(), "No starred messages on screen")
