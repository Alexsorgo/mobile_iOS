from configs import config
from screens.chats.chat_screen import ChatScreen
from screens.chats.storage_screen import StorageScreen
from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from screens.group.group_list_screen import GroupListScreen
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC15394(BaseTest):
    """
    User has the ability select few images and send them with compression to group chat
    """
    GROUP_NAME = config.GROUP_NAME
    SELECT_NUMBER = 11

    def test_c15394(self):
        log.info("Select '{}' images and send it to the group chat".format(str(self.SELECT_NUMBER)))
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        profile = OtherProfileScreen(self.driver)
        storage = StorageScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.tap_open_profile()
        profile.open_storage()
        exist_images_in_chat = storage.get_count_images()
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.tap_filter_photo()
        gallery.multiselect(self.SELECT_NUMBER)
        gallery.tap_send_btn()
        chat.tap_open_profile()
        profile.open_storage()

        log.info("Verify '{}' images sent to the chat".format(str(self.SELECT_NUMBER)))
        actual = storage.get_count_images(exist_images_in_chat)
        Verify.equals(self.SELECT_NUMBER, actual, "Not all images sent to the chat")
