from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.gallery.gallery_screen import GalleryScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC11221(BaseTest):
    """
    User has the ability send photo without compressing (as a file) with airplane mode
    """
    FRIEND = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME
    MESSAGE_TYPE = 'file'
    SEND_STATUS = 'Delivered'

    def test_c11221(self):
        log.info("Send photo without compressing (as a file) with airplane mode")
        menu = Menu(self.driver)
        gallery = GalleryScreen(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_image()
        gallery.open_curtain()
        gallery.tap_send_as_file()

        log.info("Verify media message sent without compressing (as a file)")
        Verify.true(chat.is_file_message_displayed(), "No sent file message in list")

        chat.airplane_mode()
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND)
        chat.scroll_down_try()

        log.info("Verify message status updated")
        Verify.true(chat.get_send_status(self.MESSAGE_TYPE), "Message status not updated")
