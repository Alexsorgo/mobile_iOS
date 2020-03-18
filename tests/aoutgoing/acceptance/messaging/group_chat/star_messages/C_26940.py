from configs import config
from enums import messages_enums
from screens.chats.chat_screen import ChatScreen
from screens.gallery.gallery_screen import GalleryScreen
from screens.group.group_list_screen import GroupListScreen
from screens.home_screen import HomeScreen
from controls.menu import Menu
from screens.stared_screen import StarredScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26940(BaseTest):
    """
    User has the ability star file message from group chat
    and the message displayed on stared screen
    """

    CHAT_NAME = config.GROUP_NAME + ' @ ' + config.CHINA_FIRSTNAME + ' ' + config.CHINA_LASTNAME
    FILE = messages_enums.FILE_NAME
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    GROUP_NAME = config.GROUP_NAME

    def test_c26940(self):
        log.info("Star file message: '{}'".format(self.CHAT_NAME))
        main = HomeScreen(self.driver)
        star = StarredScreen(self.driver)
        menu = Menu(self.driver)
        chat = ChatScreen(self.driver)
        gallery = GalleryScreen(self.driver)
        group_list = GroupListScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.MEDIA], menu.wenums.CHATS,
                   menu.wenums.GO_TO_GALLERY)
        gallery.open_preview_image()
        gallery.open_curtain()
        gallery.tap_send_as_file()
        chat.open_context_menu_last_bubble()
        chat.tap_context_star()
        menu.long_press_wheel()
        main.open_starred_section()

        log.info("Verify stared file message displayed on star screen")
        Verify.true(star.is_message_star_displayed(self.CHAT_NAME, self.FILE),
                    "No starred file message on screen")
