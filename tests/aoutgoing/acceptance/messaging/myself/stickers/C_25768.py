from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25768(BaseTest):

    """
    User has the ability to send sticker message in myself chat
    """

    def test_c25768(self):
        log.info("Send sticker message in myself chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        chat.tap_sticker_btn()
        chat.send_first_sticker()

        log.info("Verify sticker message display")
        Verify.true(chat.is_sticker_displayed(), "No sent message in list")
