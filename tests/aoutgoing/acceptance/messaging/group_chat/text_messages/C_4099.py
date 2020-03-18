from configs import config
from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC4099(BaseTest):

    """
    User has the ability to send schedule text message in group chat
    """
    GROUP_NAME = config.GROUP_NAME
    SCHEDULE_MESSAGE = magic.get_text_message

    def test_c4099(self):
        log.info("Send schedule text message in group chat")
        menu = Menu(self.driver)
        home = HomeScreen(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.SCHEDULE_MESSAGE)
        chat.create_scheduled_message()
        chat.tap_save()
        menu.long_press_wheel()

        log.info("Verify schedule text message created")
        Verify.true(home.is_schedule_display(self.SCHEDULE_MESSAGE), "Schedule message doesn't create")
