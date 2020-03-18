import pytest

from configs import config
from screens.channels.create_channel_screen import CreateChannelScreen
from controls.menu import Menu
from screens.channels.subscribers import SubscribersScreen
from screens.chats.base_chat_screen import BaseChatScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC19273(BaseTest):
    """
    User has the ability to create channel chat with default link
    """
    CHANNEL_NAME = config.CHANNEL_NAME

    def test_c19273(self):
        log.info("Create channel with name: '{}'".format(self.CHANNEL_NAME))
        menu = Menu(self.driver)
        channel = CreateChannelScreen(self.driver)
        subscribers = SubscribersScreen(self.driver)
        chat = BaseChatScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.NEW_CHANNEL])
        channel.set_channel_name(self.CHANNEL_NAME)
        channel.create_random_link()
        channel.tap_create_channel()
        subscribers.tap_next_button()

        log.info("Verify channel created")
        Verify.true(chat.is_channel_created(), "Channel doesn't created")
