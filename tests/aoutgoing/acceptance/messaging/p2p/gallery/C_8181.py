from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC8181(BaseTest):
    """
    User has the ability to open gallery screen from chat
    """
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c8181(self):
        log.info("Open custom gallery from chat")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)

        log.info("Verify gallery screen displayed")
        Verify.true(gallery.is_gallery_screen(), "Gallery screen doesn't display")
