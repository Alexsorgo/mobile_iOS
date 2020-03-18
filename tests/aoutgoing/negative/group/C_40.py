from configs import config
from screens.group.group_screen import GroupScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC40(BaseTest):
    """
    User has no the ability to create group chat with chat name more then 32 char
    """
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    MAX_GROUP_NAME = config.MAX_GROUP_NAME

    def test_c40(self):
        log.info("Create group with group name more then 32 char")
        menu = Menu(self.driver)
        group = GroupScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.NEW_GROUP])
        group.add_user(self.FRIEND)
        group.tap_done()
        group.tap_group_name()
        group.set_group_name(self.MAX_GROUP_NAME)

        log.info("Verify group name length")
        Verify.true(len(group.input_value()) == 32, "Group name more then 32 char")
