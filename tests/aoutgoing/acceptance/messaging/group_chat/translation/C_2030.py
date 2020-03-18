from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC2030(BaseTest):
    """
    User has the ability untranslate aoutgoing message in group chat
    """

    MESSAGE = 'Доброе утро'
    TRANSLATED_MESSAGE = 'Good morning'
    GROUP_NAME = config.GROUP_NAME

    def test_c2030(self):
        log.info("Translate message: '{}'".format(self.MESSAGE))
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.MESSAGE)
        chat.tap_context_translate()
        chat.open_context_menu(self.MESSAGE)
        chat.tap_context_untranslate()

        log.info("Verify message untranslated")
        actual = chat.get_text_msg()
        Verify.equals([self.MESSAGE], actual, "No untranslated messages on screen")
