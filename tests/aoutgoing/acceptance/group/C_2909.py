from configs import config
from screens.group.group_screen import GroupScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2909(BaseTest):
    """
    Check that default alias in Group is match with First / Last name is user doesn't set a username
    """
    ALIAS = magic.get_word
    MY_USERNAME = config.CHINA_FIRSTNAME + ' ' + config.CHINA_LASTNAME
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c2909(self):
        log.info("Create group with default alias")
        menu = Menu(self.driver)
        group = GroupScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.NEW_GROUP])
        group.add_user(self.FRIEND)
        group.tap_done()

        log.info("Verify alias is match with First / Last name ")
        Verify.true(group.default_alias(self.MY_USERNAME), "Alias doesn't match")
