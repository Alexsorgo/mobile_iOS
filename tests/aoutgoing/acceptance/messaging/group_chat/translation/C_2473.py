from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from screens.language_settings_screen import LanguageSettingsScreen
from controls.menu import Menu
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC2473(BaseTest):
    """
    User has the ability turn on autotranslation in Group for aoutgoing messages
    """

    GROUP_NAME = config.GROUP_NAME
    LANGUAGE = 'English'
    MESSAGE = 'Пока'
    TRANSLATED_MESSAGE = 'Until'

    def test_c2473(self):
        log.info("Auto translate of aoutgoing message in Group chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        other_profile = OtherProfileScreen(self.driver)
        language = LanguageSettingsScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.tap_open_profile()
        other_profile.open_language_settings()
        language.is_language_screen()
        language.set_autotranslate_on_sending()
        # TODO: Make scroll in group settings
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()

        log.info("Verify message translated")
        expected = [self.MESSAGE, self.TRANSLATED_MESSAGE]
        actual = chat.get_translated_msg()
        Verify.equals(expected, actual, "No translated messages on screen")
