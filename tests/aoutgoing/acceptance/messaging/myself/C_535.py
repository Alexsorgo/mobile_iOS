from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC535(BaseTest):
    """
    User has the ability to send media from gallery message in myself chat
    """

    def test_c535(self):
        log.info("Send message in myself")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS)
        menu.tap_first_media()

        log.info("Verify media message sent.")
        Verify.true(chat.is_image_displayed(), "No sent camera shot message in list")
