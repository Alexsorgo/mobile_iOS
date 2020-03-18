import pytest

from configs import config
from screens.channels.channels_list_screen import ChannelsListScreen
from screens.chats.chat_screen import ChatScreen
from screens.chats.location_screen import LocationScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC21535(BaseTest):
    """
    User has the ability to send location message in channel
    """
    CHANNEL_NAME = config.CHANNEL_NAME

    def test_c21535(self):
        log.info("Send location message in channel")
        menu = Menu(self.driver)
        location = LocationScreen(self.driver)
        chat = ChatScreen(self.driver)
        channels = ChannelsListScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.MY_CHANNELS])
        channels.open_channel(self.CHANNEL_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.LOCATION, menu.wenums.SEND_LOCATION], menu.wenums.CHATS)
        location.tap_send_location()

        log.info("Verify location message sent.")
        Verify.true(chat.is_location_displayed(), "No sent message in list")
