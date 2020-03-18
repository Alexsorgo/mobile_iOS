from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.camera_screen import CameraScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC1791(BaseTest):
    """
    User has the ability to send camera video message in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c1791(self):
        log.info("Send video message in group chat")
        chat = ChatScreen(self.driver)
        menu = Menu(self.driver)
        camera = CameraScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CAMERA], menu.wenums.CHATS)
        camera.tap_video_camera()
        camera.record_video()
        camera.tap_send_button()

        log.info("Verify video message sent.")
        Verify.true(chat.is_video_displayed(), "No sent video message in list")
