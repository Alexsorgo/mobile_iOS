from screens.gallery.gallery_screen import GalleryScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.profile_screen import ProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26(BaseTest):
    """
    User has the ability to set own avatar photo
    """
    def test_c26(self):
        log.info("Set avatar photo")
        home = HomeScreen(self.driver)
        profile = ProfileScreen(self.driver)
        gallery = GalleryScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.EDIT_PROFILE, menu.wenums.MY_PHOTO], menu.wenums.CHATS)
        profile.tap_photo_form_gallery()
        gallery.select_avatar()
        profile.tap_accept_photo()

        log.info("Verify avatar photo is updated successfully.")
        Verify.true(home.is_avatar_updated(), "The avatar photo is not updated")
