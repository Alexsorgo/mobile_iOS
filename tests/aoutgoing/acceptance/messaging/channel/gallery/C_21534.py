import pytest

from configs import config
from screens.channels.channels_list_screen import ChannelsListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC21534(BaseTest):
    """
    User has the ability to send media from gallery message in channel
    """
    CHANNEL_NAME = config.CHANNEL_NAME

    def test_c21534(self):
        log.info("Send media message in channel")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        channels = ChannelsListScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.MY_CHANNELS])
        channels.open_channel(self.CHANNEL_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA, menu.wenums.GALLERY], menu.wenums.CHATS)
        menu.tap_first_media()

        log.info("Verify media message sent.")
        Verify.true(chat.is_image_displayed(), "No sent camera shot message in list")
