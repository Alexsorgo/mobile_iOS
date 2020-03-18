from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from screens.group.group_options_screen import GroupOptionScreen
from screens.group.group_screen import GroupScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2906(BaseTest):
    """
    User has the ability to edit group name
    """
    GROUP_NAME = magic.get_word

    def test_c2906(self):
        log.info("Edit group name")
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        chat = ChatScreen(self.driver)
        group = GroupScreen(self.driver)
        options = GroupOptionScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_first_group()
        chat.tap_open_profile()
        options.open_group_name()
        group.set_group_name(self.GROUP_NAME)
        group.tap_save()

        log.info("Verify group name updated")
        Verify.true(options.verify_element(self.GROUP_NAME), "Group name doesn't updated")
