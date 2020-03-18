from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from screens.chats.location_screen import LocationScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC1793(BaseTest):
    """
    User has the ability to send location message in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c1793(self):
        log.info("Send location message in group chat")
        chat = ChatScreen(self.driver)
        menu = Menu(self.driver)
        location = LocationScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.LOCATION], menu.wenums.CHATS)
        location.tap_send_location()

        log.info("Verify location message sent.")
        Verify.true(chat.is_location_displayed(), "No sent message in list")
