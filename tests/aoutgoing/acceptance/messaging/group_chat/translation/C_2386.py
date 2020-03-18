from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from screens.language_settings_screen import LanguageSettingsScreen
from controls.menu import Menu
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC2386(BaseTest):
    """
    User has the ability select another language for translation in group chat for aoutgoing messages
    """

    GROUP_NAME = config.GROUP_NAME
    LANGUAGE = 'English'

    def test_c2386(self):
        log.info("Ser '{}' language for aoutgoing messages".format(self.LANGUAGE))
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
        language.open_on_sending()
        language.tap_search_result(self.LANGUAGE)
        # TODO: Make scroll in group settings
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)

        log.info("Verify language curtain displayed")
        Verify.true(chat.is_curtain_display(), "Language curtain is not displayed")
