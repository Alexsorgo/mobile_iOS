from configs import config
from enums import messages_enums
from screens.chats.chat_screen import ChatScreen
from screens.group.group_list_screen import GroupListScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.stared_screen import StarredScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26936(BaseTest):
    """
    User has the ability star voice message from group chat and the message displayed on stared screen
    """

    CHAT_NAME = config.GROUP_NAME + ' @ ' + config.CHINA_FIRSTNAME + ' ' + config.CHINA_LASTNAME
    VOICE = messages_enums.VOICE_NAME
    GROUP_NAME = config.GROUP_NAME

    def test_c26936(self):
        log.info("Star message: '{}'".format(self.CHAT_NAME))
        main = HomeScreen(self.driver)
        star = StarredScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        chat.record_voice_msg()
        chat.tap_record_send()
        chat.open_context_menu_last_bubble()
        chat.tap_context_star()
        menu.long_press_wheel()
        main.open_starred_section()

        log.info("Verify stared voice message displayed on star screen")
        Verify.true(star.is_message_star_displayed(self.CHAT_NAME, self.VOICE), "No starred voice message on screen")
