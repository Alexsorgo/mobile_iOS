from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.chats.storage_screen import StorageScreen
from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC8186(BaseTest):
    """
    User has the ability select few images and send them with compression to private chat
    """
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    SELECT_NUMBER = 11

    def test_c8186(self):
        log.info("Select '{}' images and send it to the private chat".format(str(self.SELECT_NUMBER)))
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        profile = OtherProfileScreen(self.driver)
        storage = StorageScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.tap_open_profile()
        profile.open_storage()
        exist_images_in_chat = storage.get_count_images()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
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
