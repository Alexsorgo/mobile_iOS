from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.contact_screen import ContactScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC11220(BaseTest):
    """
    User has the ability to send contact message in p2p chat with airplane mode
    """
    FRIEND = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME
    MESSAGE_TYPE = 'contact'
    SEND_STATUS = 'Delivered'

    def test_c11220(self):
        log.info("Send contact message in p2p chat with airplane mode")
        menu = Menu(self.driver)
        chat_list = ChatListScreen(self.driver)
        contact = ContactScreen(self.driver)
        chat = ChatScreen(self.driver)
        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CONTACT], menu.wenums.CHATS)
        contact.tap_contact(self.FRIEND)

        log.info("Verify contact message sent.")
        Verify.true(chat.is_contact_share(self.FRIEND), "No contact message in list")

        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.scroll_down_try()

        log.info("Verify message status updated")
        Verify.true(chat.get_send_status(self.MESSAGE_TYPE), "Message status not updated")
