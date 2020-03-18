from configs import config
from enums import context_enums
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.stared_screen import StarredScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC7369(BaseTest):
    """
    User has the ability call unstar menu on starred screen
    """

    STARED_MESSAGE = magic.get_text_message
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c7369(self):
        log.info("Unstar message: '{}'".format(self.STARED_MESSAGE))
        main = HomeScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        star = StarredScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_option(context_enums.STAR)
        menu.long_press_wheel()
        main.open_starred_section()
        star.open_context(self.STARED_MESSAGE)

        log.info("Verify Unstar context menu displayed")
        Verify.true(star.is_context_option_unstar_displayed(), "Unstar context menu doesn't display")
