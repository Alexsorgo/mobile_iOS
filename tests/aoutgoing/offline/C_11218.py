from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC11218(BaseTest):
    """
    User has the ability to send media from gallery message in p2p chat with airplane mode
    """
    FRIEND = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME
    MESSAGE_TYPE = 'image'
    SEND_STATUS = 'Delivered'

    def test_c11218(self):
        log.info("Send media message in p2p chat with airplane mode")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS)
        menu.tap_first_media()

        log.info("Verify media message sent.")
        Verify.true(chat.is_image_displayed(), "No sent camera shot message in list")

        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.scroll_down_try()

        log.info("Verify message status updated")
        Verify.true(chat.get_send_status(self.MESSAGE_TYPE), "Message status not updated")
