import pytest

from configs import config
from screens.channels.channels_list_screen import ChannelsListScreen
from screens.chats.camera_screen import CameraScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC21533(BaseTest):
    """
    User has the ability to send camera video message in channel
    """
    CHANNEL_NAME = config.CHANNEL_NAME

    def test_c21533(self):
        log.info("Send video message in channel")
        camera = CameraScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        channels = ChannelsListScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.MY_CHANNELS])
        channels.open_channel(self.CHANNEL_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CAMERA], menu.wenums.CHATS)
        camera.tap_video_camera()
        camera.record_video()
        camera.tap_send_button()

        log.info("Verify video message displayed")
        Verify.true(chat.is_image_displayed(), "No sent video message in list")
