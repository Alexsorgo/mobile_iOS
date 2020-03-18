from screens.gallery.gallery_screen import GalleryScreen
from screens.gallery.preview_gallery_screen import PreviewGalleryScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25392(BaseTest):
    """
    Send as file button present on full image view from gallery in myself chat
    """

    def test_c25392(self):
        log.info("Open first image preview from gallery in myself chat")
        gallery = GalleryScreen(self.driver)
        gallery_preview = PreviewGalleryScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_image()
        gallery_preview.open_curtain()

        log.info("Verify send as file button display")
        Verify.true(gallery_preview.is_send_as_file_btn_display(), "Send as file button doesn't display")
