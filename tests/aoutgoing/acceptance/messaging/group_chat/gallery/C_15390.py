from configs import config
from screens.gallery.gallery_screen import GalleryScreen
from screens.gallery.preview_gallery_screen import PreviewGalleryScreen
from screens.group.group_list_screen import GroupListScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC15390(BaseTest):
    """
    User has the ability to open full image view from gallery in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c15390(self):
        log.info("Open first image preview from gallery in group chat")
        gallery = GalleryScreen(self.driver)
        gallery_preview = PreviewGalleryScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_image()

        log.info("Verify full image view from gallery displayed")
        Verify.true(gallery_preview.is_full_view_open(), "Full image view from gallery doesn't display")
