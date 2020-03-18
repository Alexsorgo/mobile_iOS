from configs import config
from enums import messages_enums
from screens.chats.chat_list_screen import ChatListScreen
from screens.chats.chat_screen import ChatScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.stared_screen import StarredScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26929(BaseTest):
    """
    User has the ability star message from p2p chat and the message displayed on stared screen
    """

    CHAT_NAME = config.CHINA_FIRSTNAME + ' ' + config.CHINA_LASTNAME
    VOICE = messages_enums.VOICE_NAME
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c26929(self):
        log.info("Star message: '{}'".format(self.CHAT_NAME))
        main = HomeScreen(self.driver)
        star = StarredScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        chat_list = ChatListScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        chat_list.tap_user(self.FRIEND_NAME)
        chat.record_voice_msg()
        chat.tap_record_send()
        chat.open_context_menu_last_bubble()
        chat.tap_context_star()
        menu.long_press_wheel()
        main.open_starred_section()

        log.info("Verify stared voice message displayed on star screen")
        Verify.true(star.is_message_star_displayed(self.CHAT_NAME, self.VOICE), "No starred voice message on screen")
