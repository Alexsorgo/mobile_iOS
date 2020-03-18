from screens.chats.chat_screen import ChatScreen
from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25398(BaseTest):
    """
    User has the ability to send video as file from custom gallery preview
    """

    def test_c25398(self):
        log.info("Sending video as file from preview")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_video()
        gallery.open_curtain()
        gallery.tap_send_as_file()

        log.info("Verify video sent as file from preview")
        Verify.true(chat.is_file_message_displayed(), "Video doesn't sent as file")
