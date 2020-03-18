from enums import error_enums
from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from screens.group.group_options_screen import GroupOptionScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26923(BaseTest):
    """
    User has no the ability to delete and exit from chat if he's one admin in group
    """
    ALIAS = magic.get_word
    ALERT = error_enums.DELETE_GROUP

    def test_c26923(self):
        log.info("Try leave group if user admin")
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        chat = ChatScreen(self.driver)
        options = GroupOptionScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_first_group()
        chat.tap_open_profile()
        options.delete_and_leave()

        log.info("Verify alert '{}' displayed".format(self.ALERT))
        Verify.true(options.error_verify(self.ALERT), "Alert doesn't displayed")
