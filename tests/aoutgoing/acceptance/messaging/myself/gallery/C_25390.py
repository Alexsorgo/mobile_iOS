from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC25390(BaseTest):
    """
    User has the ability to open gallery screen from myself
    """

    def test_c25390(self):
        log.info("Open custom gallery from myself")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)

        log.info("Verify gallery screen displayed")
        Verify.true(gallery.is_gallery_screen(), "Gallery screen doesn't display")
