from configs import config
from enums import error_enums
from screens.group.group_screen import GroupScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC39(BaseTest):
    """
    User has the ability to create group chat with 1 more user
    """
    EMPTY_NAME = ''
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c39(self):
        log.info("Create group with empty group name")
        menu = Menu(self.driver)
        group = GroupScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.NEW_GROUP])
        group.add_user(self.FRIEND)
        group.tap_done()
        group.tap_group_name()
        group.set_group_name(self.EMPTY_NAME)
        group.tap_save()

        log.info("Verify group doesn't create")
        Verify.true(group.error_verify(error_enums.GROUP_NAME_MIN), "Group created")
