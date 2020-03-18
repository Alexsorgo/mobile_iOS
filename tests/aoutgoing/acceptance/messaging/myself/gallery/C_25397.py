from screens.chats.chat_screen import ChatScreen
from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25397(BaseTest):
    """
    User has the ability to send video message from custom gallery preview
    """

    def test_c25397(self):
        log.info("Sending video from preview")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_video()
        gallery.tap_send_btn()

        log.info("Verify video sent from preview ")
        Verify.true(chat.is_video_displayed(), "Video doesn't sent")
