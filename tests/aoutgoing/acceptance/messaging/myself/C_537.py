from screens.chats.camera_screen import CameraScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC537(BaseTest):
    """
    User has the ability to send camera photo message in myself chat
    """

    def test_c537(self):
        log.info("Send message in myself")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        camera = CameraScreen(self.driver)
        menu.go_to(menu.wenums.MYSELF)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CAMERA], menu.wenums.CHATS)
        camera.tap_take_photo()
        camera.tap_send_button()

        log.info("Verify camera photo message sent.")
        Verify.true(chat.is_image_displayed(), "No sent camera shot message in list")
