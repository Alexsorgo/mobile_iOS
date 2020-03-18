from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.language_settings_screen import LanguageSettingsScreen
from controls.menu import Menu
from screens.other_profile_screen import OtherProfileScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC2472(BaseTest):
    """
    User has the ability turn on autotranslation in P2P for aoutgoing messages
    """

    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    LANGUAGE = 'English'
    MESSAGE = 'Пока'
    TRANSLATED_MESSAGE = 'Until'

    def test_c2472(self):
        log.info("Auto translate of aoutgoing message in P2P")
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
        language.set_autotranslate_on_sending()
        language.tap_back()
        other_profile.tap_send_message()
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()

        log.info("Verify message translated")
        expected = [self.MESSAGE, self.TRANSLATED_MESSAGE]
        actual = chat.get_translated_msg()
        Verify.equals(expected, actual, "No translated messages on screen")
