from configs import config
from screens.group.group_screen import GroupScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC38(BaseTest):
    """
    User has the ability to create group chat with 1 more user
    """
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME
    GROUP_NAME = config.GROUP_NAME

    def test_c38(self):
        log.info("Create group chat with name: '{}'".format(config.GROUP_NAME))
        menu = Menu(self.driver)
        group = GroupScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.NEW_GROUP])
        group.add_user(self.FRIEND)
        group.tap_done()
        group.tap_group_name()
        group.set_group_name(self.GROUP_NAME)
        group.tap_save()
        group.tap_create()

        log.info("Verify group created")
        Verify.true(group.is_group_created(),
                    "No group created")
