from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.stared_screen import StarredScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC1932(BaseTest):
    """
    User has the ability star message from p2p chat and the message displayed on stared screen
    """

    STARED_MESSAGE = magic.get_text_message
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c1932(self):
        log.info("Star message: '{}'".format(self.STARED_MESSAGE))
        main = HomeScreen(self.driver)
        star = StarredScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_star()
        menu.long_press_wheel()
        main.open_starred_section()

        log.info("Verify stared message displayed on star screen")
        Verify.true(star.is_starred_message_displayed(self.STARED_MESSAGE), "No starred messages on screen")
