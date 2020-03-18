from configs import config
from screens.chats.chat_screen import ChatScreen
from screens.group.group_screen import GroupScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC4102(BaseTest):
    """
    User has the ability to see alias inserted as a link in the input field
    """

    GROUP_NAME = magic.get_word
    MESSAGE = magic.get_text_message
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c4102(self):
        log.info("Alias inserted as a link in the input field ")
        menu = Menu(self.driver)
        group = GroupScreen(self.driver)
        chat = ChatScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.NEW_GROUP])
        group.add_user(self.FRIEND)
        group.tap_done()
        group.tap_group_name()
        group.set_group_name(self.GROUP_NAME)
        group.tap_save()
        group.tap_create()
        chat.tap_first_mention()
        chat.set_msg_without_clear(self.MESSAGE)
        chat.tap_send_btn()

        log.info("Verify mention displayed")
        Verify.true(chat.is_mention_present(), "No mention in the message")
