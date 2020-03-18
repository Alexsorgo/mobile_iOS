from configs import config
from screens.gallery.gallery_screen import GalleryScreen
from screens.group.group_list_screen import GroupListScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC15389(BaseTest):
    """
    User has the ability to open gallery screen from group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c15389(self):
        log.info("Open custom gallery from group chat")
        gallery = GalleryScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)

        log.info("Verify gallery screen displayed")
        Verify.true(gallery.is_gallery_screen(), "Gallery screen doesn't display")
