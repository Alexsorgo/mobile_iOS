import pytest

from configs import config
from screens.channels.channels_list_screen import ChannelsListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC21531(BaseTest):
    """
    User has the ability to send voice message in channel
    """
    CHANNEL_NAME = config.CHANNEL_NAME

    def test_c21531(self):
        log.info("Send voice message in channel")
        menu = Menu(self.driver)
        channels = ChannelsListScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.MY_CHANNELS])
        channels.open_channel(self.CHANNEL_NAME)
        chat = ChatScreen(self.driver)
        chat.record_voice_msg()
        chat.tap_record_send()

        log.info("Verify voice message sent.")
        Verify.true(chat.is_voice_displayed(), "No sent voice message in list")
