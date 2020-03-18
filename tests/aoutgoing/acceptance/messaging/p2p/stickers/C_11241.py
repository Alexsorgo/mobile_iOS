from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC11241(BaseTest):

    """
    User has the ability to send sticker message in p2p chat
    """
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c11241(self):
        log.info("Send sticker message in p2p chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.tap_sticker_btn()
        chat.send_first_sticker()

        log.info("Verify sticker message display")
        Verify.true(chat.is_sticker_displayed(), "No sent message in list")
