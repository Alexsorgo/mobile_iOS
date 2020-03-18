from screens.chats.chat_screen import ChatScreen
from screens.group.alias_screen import AliasScreen
from screens.group.group_list_screen import GroupListScreen
from screens.group.group_options_screen import GroupOptionScreen
from screens.group.participants_screen import ParticipantsScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2903(BaseTest):
    """
    User has the ability to see updated alias on group admins screen
    """
    ALIAS = magic.get_word

    def test_c2903(self):
        log.info("Check updated alias displayed on admins screen")
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        chat = ChatScreen(self.driver)
        options = GroupOptionScreen(self.driver)
        alias = AliasScreen(self.driver)
        participants = ParticipantsScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_first_group()
        chat.tap_open_profile()
        options.open_alias()
        alias.set_alias(self.ALIAS)
        options.open_group_admins()

        log.info("Verify updated alias displayed on group admins screen")
        Verify.true(participants.is_participant_updated(self.ALIAS), "Alias doesn't update on screen")
