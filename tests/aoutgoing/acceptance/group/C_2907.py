from screens.chats.chat_screen import ChatScreen
from screens.group.alias_screen import AliasScreen
from screens.group.group_list_screen import GroupListScreen
from screens.group.group_options_screen import GroupOptionScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2907(BaseTest):
    """
    User has no the ability to see updated alias on group options screen
    """
    ALIAS = magic.get_word

    def test_c2907(self):
        log.info("Update alias and check new alias on group options screen")
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        chat = ChatScreen(self.driver)
        options = GroupOptionScreen(self.driver)
        alias = AliasScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_first_group()
        chat.tap_open_profile()
        options.open_alias()
        alias.set_alias(self.ALIAS)

        log.info("Verify updated alias displayed on group options screen")
        Verify.true(options.verify_element(self.ALIAS), "Alias doesn't update on screen")
