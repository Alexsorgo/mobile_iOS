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
class TestC21536(BaseTest):
    """
    User has the ability to reply text message in channel
    """

    CHANNEL_NAME = config.CHANNEL_NAME
    TEXT_MESSAGE = magic.get_text_message
    REPLY_MESSAGE = magic.get_text_message

    def test_c21536(self):
        log.info("Send and reply message in channel")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        channels = ChannelsListScreen(self.driver)
        menu.go_to(menu.wenums.CHANNELS, [menu.wenums.MY_CHANNELS])
        channels.open_channel(self.CHANNEL_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_reply()
        chat.set_chat_msg(self.REPLY_MESSAGE)
        chat.tap_send_btn()

        log.info("Verify text message replied.")
        Verify.true(chat.is_replay_displayed(self.TEXT_MESSAGE, self.REPLY_MESSAGE), "No replied message in list")
