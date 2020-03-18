from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from screens.group.group_options_screen import GroupOptionScreen
from screens.group.participants_screen import ParticipantsScreen
from controls.menu import Menu
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2908(BaseTest):
    """
    User has the ability go to the other user profile from participant screen
    """
    ALIAS = magic.get_word

    def test_c2908(self):
        log.info("Go to other user profile from participant screen")
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        chat = ChatScreen(self.driver)
        participants = ParticipantsScreen(self.driver)
        profile = OtherProfileScreen(self.driver)
        options = GroupOptionScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_first_group()
        chat.tap_open_profile()
        options.open_group_participants()
        participants.open_participant()

        log.info("Verify other user profile displayed")
        Verify.true(profile.is_profile_displayed(), "Other user profile doesn't displayed")
