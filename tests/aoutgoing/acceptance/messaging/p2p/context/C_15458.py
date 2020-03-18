import pytest

from configs import config
from enums import context_enums
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.contact_screen import ContactScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


@pytest.mark.skip
class TestC4103(BaseTest):
    """
    Check context menu items on contact message in p2p chat
    """

    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c4103(self):
        log.info("Check context menu items on contact message in p2p chat")
        menu = Menu(self.driver)
        chat_list = ChatListScreen(self.driver)
        contact = ContactScreen(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CONTACT], menu.wenums.CHATS)
        contact.tap_contact(self.FRIEND)
        chat.open_context_menu_last_bubble()

        log.info("Verify context menu items")
        Verify.equals(context_enums.CONTACT_CONTEXT_MENU_ITEMS, chat.get_context_options(),
                      "Wrong context menu items")
