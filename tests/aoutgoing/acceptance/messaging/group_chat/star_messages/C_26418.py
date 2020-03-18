from configs import config
from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26418(BaseTest):
    """
    User has the ability star message from group chat
    """
    GROUP_NAME = config.GROUP_NAME
    STARED_MESSAGE = magic.get_text_message

    def test_c26418(self):
        log.info("Star message: '{}'".format(config.STARED_MESSAGE))
        main = HomeScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_star()
        menu.long_press_wheel()
        main.tap_stared_msg(self.STARED_MESSAGE)

        log.info("Verify that message stared")
        Verify.true(chat.stared_present(), "No starred messages on screen")
