from configs import config
from screens.chats.camera_screen import CameraScreen
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC35(BaseTest):
    """
    User has the ability to send camera video message in p2p chat
    """
    FULL_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c35(self):
        log.info("Send video message in p2p chat")
        camera = CameraScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CAMERA], menu.wenums.CHATS)
        camera.tap_video_camera()
        camera.record_video()
        camera.tap_send_button()

        log.info("Verify video message sent.")
        Verify.true(chat.is_video_displayed(), "No sent video message in list")
