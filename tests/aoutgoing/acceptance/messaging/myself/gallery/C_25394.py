from screens.chats.chat_screen import ChatScreen
from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25394(BaseTest):
    """
    User has the ability send photo without compressing (as a file)
    """

    def test_c25394(self):
        log.info("Send photo without compressing (as a file)")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_image()
        gallery.open_curtain()
        gallery.tap_send_as_file()

        log.info("Verify media message sent without compressing (as a file)")
        Verify.true(chat.is_file_message_displayed(), "No sent file message in list")
