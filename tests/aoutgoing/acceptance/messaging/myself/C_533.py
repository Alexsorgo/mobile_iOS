from screens.chats.camera_screen import CameraScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC533(BaseTest):
    """
    User has the ability to send camera video message in myself chat
    """

    def test_c533(self):
        log.info("Send video message in myself")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        camera = CameraScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CAMERA], menu.wenums.CHATS)
        camera.tap_video_camera()
        camera.record_video()
        camera.tap_send_button()

        log.info("Verify video message sent.")
        Verify.true(chat.is_video_displayed(), "No sent video message in list")
