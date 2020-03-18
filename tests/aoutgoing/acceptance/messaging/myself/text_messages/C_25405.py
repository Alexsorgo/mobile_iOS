from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.chats.forward_screen import ForwardScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC25405(BaseTest):
    """
    User has the ability to send forward message to myself chat
    """
    TEXT_MESSAGE = magic.get_text_message
    FRIEND_USERNAME = config.AMERICA_USERNAME
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    MYSELF_USERNAME = config.CHINA_FIRSTNAME + ' ' + config.CHINA_LASTNAME

    def test_c25405(self):
        log.info("Send forward message to myself chat")
        menu = Menu(self.driver)
        forward = ForwardScreen(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_forward()
        forward.select_forward(self.MYSELF_USERNAME)
        forward.tap_send_btn()
        menu.go_to(menu.wenums.MYSELF)

        log.info("Verify forward message displayed")
        Verify.true(chat.is_forward_present(self.TEXT_MESSAGE), "No forward message om screen")
