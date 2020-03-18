from configs import config
from screens.chats.chat_screen import ChatScreen
from screens.gallery.gallery_screen import GalleryScreen
from screens.group.group_list_screen import GroupListScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC15397(BaseTest):
    """
    User has the ability to send video as file from custom gallery preview
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c15397(self):
        log.info("Sending video as file from preview")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_video()
        gallery.open_curtain()
        gallery.tap_send_as_file()

        log.info("Verify video sent as file from preview")
        Verify.true(chat.is_file_message_displayed(), "Video doesn't sent as file")
