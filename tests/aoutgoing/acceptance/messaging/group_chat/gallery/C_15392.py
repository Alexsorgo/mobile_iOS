from configs import config
from screens.chats.chat_screen import ChatScreen
from screens.gallery.gallery_screen import GalleryScreen
from screens.group.group_list_screen import GroupListScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC15392(BaseTest):
    """
    User has the ability Send photo with compression
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c15392(self):
        log.info("Select one image and send it to the private chat with compression")
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.tap_filter_photo()
        gallery.select_image()
        gallery.tap_send_btn()

        log.info("Verify image sent with compression")
        Verify.true(chat.is_compressed(), "Last image not compressed")
