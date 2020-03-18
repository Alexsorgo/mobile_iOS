import pytest

from configs import config
from screens.channels.channels_list_screen import ChannelsListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC21568(BaseTest):

    """
    User has the ability to send sticker message in channel
    """
    CHANNEL_NAME = config.CHANNEL_NAME

    def test_c21568(self):
        log.info("Send sticker message in channel")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        channels = ChannelsListScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.MY_CHANNELS])
        channels.open_channel(self.CHANNEL_NAME)
        chat.tap_sticker_btn()
        chat.send_first_sticker()

        log.info("Verify sticker message display")
        Verify.true(chat.is_sticker_displayed(), "No sent message in list")
