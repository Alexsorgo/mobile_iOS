from configs import config
from enums import error_enums
from screens.group.create_group_screen import CreateGroupScreen
from screens.group.group_screen import GroupScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC2901(BaseTest):
    """
    User has no the ability to create group with empty alias
    """
    EMPTY_ALIAS = ''
    ALERT = error_enums.EMPTY_ALIAS
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c2901(self):
        log.info("Create group chat with empty alias")
        menu = Menu(self.driver)
        group = GroupScreen(self.driver)
        g_create = CreateGroupScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.NEW_GROUP])
        group.add_user(self.FRIEND)
        group.tap_done()
        g_create.set_alias(self.EMPTY_ALIAS)

        log.info("Verify alert displayed")
        Verify.true(g_create.error_verify(self.ALERT), "Empty alias alert doesn't displayed")
