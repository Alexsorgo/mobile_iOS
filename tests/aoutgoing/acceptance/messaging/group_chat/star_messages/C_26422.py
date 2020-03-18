from configs import config
from enums import context_enums
from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.stared_screen import StarredScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26422(BaseTest):
    """
    User has the ability unstar text message from starred screen and check that it disappear
    """

    GROUP_NAME = config.GROUP_NAME
    STARED_MESSAGE = magic.get_text_message

    def test_c26422(self):
        log.info("Unstar message: '{}'".format(self.STARED_MESSAGE))
        main = HomeScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        star = StarredScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.set_chat_msg(self.STARED_MESSAGE)
        chat.tap_send_btn()
        chat.open_context_menu(self.STARED_MESSAGE)
        chat.tap_context_option(context_enums.STAR)
        menu.long_press_wheel()
        main.open_starred_section()
        star.unstar_message(self.STARED_MESSAGE)

        log.info("Verify stared message doesn't display on starred screen")
        Verify.false(star.is_starred_message_displayed(self.STARED_MESSAGE), "Starred message still displayed")
