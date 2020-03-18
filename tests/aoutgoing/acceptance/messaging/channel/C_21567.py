import pytest

from configs import config
from screens.channels.channels_list_screen import ChannelsListScreen
from screens.chats.location_screen import LocationScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC21567(BaseTest):
    """
    User has the ability to send location message in channel
    """

    CHANNEL_NAME = config.CHANNEL_NAME
    PLACE = "Kharkiv"

    def test_c21567(self):
        log.info("Send place message in channel")
        menu = Menu(self.driver)
        channels = ChannelsListScreen(self.driver)
        location = LocationScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.MY_CHANNELS])
        channels.open_channel(self.CHANNEL_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.LOCATION, menu.wenums.SEND_LOCATION], menu.wenums.CHATS)
        location.tap_search()
        location.search_and_open_place(self.PLACE)
        location.tap_send_location()

        log.info("Verify place message sent.")
        Verify.true(location.is_place_displayed(self.PLACE), "No sent place message")
