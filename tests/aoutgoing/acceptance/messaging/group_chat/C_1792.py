from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC1792(BaseTest):
    """
    User has the ability to send media from gallery message in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c1792(self):
        log.info("Send media message in group chat")
        chat = ChatScreen(self.driver)
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS)
        menu.tap_first_media()

        log.info("Verify media message sent.")
        Verify.true(chat.is_image_displayed(), "No sent camera shot message in list")
