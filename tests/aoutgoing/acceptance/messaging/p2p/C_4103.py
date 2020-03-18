from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.contact_screen import ContactScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC4103(BaseTest):
    """
    User has the ability to send contact message in p2p chat
    """

    FULL_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c4103(self):
        log.info("Send contact message in p2p chat")
        menu = Menu(self.driver)
        chat_list = ChatListScreen(self.driver)
        contact = ContactScreen(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FULL_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CONTACT], menu.wenums.CHATS)
        contact.tap_contact(self.FULL_NAME)

        log.info("Verify contact message sent.")
        Verify.true(chat.is_contact_share(self.FULL_NAME), "No contact message in list")
