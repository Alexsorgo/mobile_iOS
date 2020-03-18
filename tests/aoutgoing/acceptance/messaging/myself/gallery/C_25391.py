from screens.gallery.gallery_screen import GalleryScreen
from screens.gallery.preview_gallery_screen import PreviewGalleryScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25391(BaseTest):
    """
    User has the ability to open full image view from gallery
    """

    def test_c25391(self):
        log.info("Open first image preview from gallery")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        gallery_preview = PreviewGalleryScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_image()

        log.info("Verify full image view from gallery displayed")
        Verify.true(gallery_preview.is_full_view_open(), "Full image view from gallery doesn't display")
