from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.language_settings_screen import LanguageSettingsScreen
from controls.menu import Menu
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC2385(BaseTest):
    """
    User has the ability select another language for translation in P2P for aoutgoing messages
    """

    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    LANGUAGE = 'English'

    def test_c2385(self):
        log.info("Ser '{}' language for aoutgoing messages".format(self.LANGUAGE))
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        other_profile = OtherProfileScreen(self.driver)
        language = LanguageSettingsScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.tap_open_profile()
        other_profile.open_language_settings()
        language.is_language_screen()
        language.open_on_sending()
        language.tap_search_result(self.LANGUAGE)
        language.tap_back()
        other_profile.tap_send_message()

        log.info("Verify language curtain displayed")
        Verify.true(chat.is_curtain_display(), "Language curtain is not displayed")
