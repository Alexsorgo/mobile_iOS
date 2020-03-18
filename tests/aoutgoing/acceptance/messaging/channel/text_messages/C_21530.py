import pytest

from configs import config
from screens.channels.channels_list_screen import ChannelsListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC21530(BaseTest):
    """
    User has the ability to send text message in channel
    """
    CHANNEL_NAME = config.CHANNEL_NAME
    TEXT_MESSAGE = magic.get_text_message

    def test_c21530(self):
        log.info("Send text message in channel")
        menu = Menu(self.driver)
        channels = ChannelsListScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.MY_CHANNELS])
        channels.open_channel(self.CHANNEL_NAME)
        chat = ChatScreen(self.driver)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify text message sent.")
        Verify.contains(self.TEXT_MESSAGE, chat.get_text_msg(), "No sent message in list")
