from configs import config
from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC11252(BaseTest):

    """
    User has the ability to send sticker message as reply in group chat
    """
    GROUP_NAME = config.GROUP_NAME
    TEXT_MESSAGE = magic.get_text_message
    REPLY_OPTION = context_enums.REPLY

    def test_c11252(self):
        log.info("Send sticker message as reply in group chat")
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.TEXT_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.TEXT_MESSAGE)
        chat.tap_context_option(self.REPLY_OPTION)
        chat.tap_sticker_btn()
        chat.send_first_sticker()

        log.info("Verify reply sticker message display")
        Verify.true(chat.is_sticker_reply(), "No sent message in list")
