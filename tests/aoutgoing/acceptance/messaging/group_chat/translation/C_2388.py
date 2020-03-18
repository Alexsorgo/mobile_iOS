from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from screens.language_settings_screen import LanguageSettingsScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2388(BaseTest):
    """
    User has the ability select another language for translation in P2P for aoutgoing messages
    """

    GROUP_NAME = config.GROUP_NAME
    MAIN_LANGUAGE_CODE = 'EN'
    EDIT_LANGUAGE_CODE = 'AZ'
    EDIT_LANGUAGE = 'Azerbaijani'
    MESSAGE = magic.get_text_message

    def test_c2388(self):
        log.info("Set '{}' language for once".format(self.EDIT_LANGUAGE))
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        language = LanguageSettingsScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.open_lang_curtain()
        chat.tap_on_language(self.MAIN_LANGUAGE_CODE)
        language.tap_search_result(self.EDIT_LANGUAGE)
        language.tap_alert_once()
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_translate_icon()
        chat.tap_send_btn()

        log.info("Verify main language set again")
        Verify.true(chat.verify_lang_code(self.MAIN_LANGUAGE_CODE), "Doesn't display main language")
