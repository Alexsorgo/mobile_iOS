from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.language_settings_screen import LanguageSettingsScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2387(BaseTest):
    """
    User has the ability for once select another language for translation in P2P for aoutgoing messages
    """

    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    MAIN_LANGUAGE_CODE = 'EN'
    EDIT_LANGUAGE_CODE = 'AZ'
    EDIT_LANGUAGE = 'Azerbaijani'
    MESSAGE = magic.get_text_message

    def test_c2387(self):
        log.info("Set '{}' language for once".format(self.EDIT_LANGUAGE))
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        language = LanguageSettingsScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.open_lang_curtain()
        chat.tap_on_language(self.MAIN_LANGUAGE_CODE)
        language.tap_search_result(self.EDIT_LANGUAGE)
        language.tap_alert_once()
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_translate_icon()
        chat.tap_send_btn()

        log.info("Verify main language set again")
        Verify.true(chat.verify_lang_code(self.MAIN_LANGUAGE_CODE), "Doesn't display main language")
