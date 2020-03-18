from screens.chats.chat_screen import ChatScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.stared_screen import StarredScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26443(BaseTest):
    """
    User has the ability star message from myself chat and the message displayed on stared screen
    """

    STARED_MESSAGE = magic.get_text_message

    def test_c26443(self):
        log.info("Star message: '{}'".format(self.STARED_MESSAGE))
        main = HomeScreen(self.driver)
        star = StarredScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_star()
        menu.long_press_wheel()
        main.open_starred_section()

        log.info("Verify stared message displayed on star screen")
        Verify.true(star.is_starred_message_displayed(self.STARED_MESSAGE), "No starred messages on screen")
