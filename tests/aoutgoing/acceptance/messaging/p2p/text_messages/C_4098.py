from configs import config
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC4098(BaseTest):

    """
    User has the ability to send schedule text message in p2p chat
    """
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    SCHEDULE_MESSAGE = magic.get_text_message

    def test_c4098(self):
        log.info("Send schedule text message in p2p chat")
        menu = Menu(self.driver)
        home = HomeScreen(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.set_chat_msg(self.SCHEDULE_MESSAGE)
        chat.create_scheduled_message()
        chat.tap_save()
        menu.long_press_wheel()

        log.info("Verify schedule text message created")
        Verify.true(home.is_schedule_display(self.SCHEDULE_MESSAGE), "Schedule message doesn't create")
