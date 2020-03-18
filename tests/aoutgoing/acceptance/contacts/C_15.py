from configs import config
from screens.add_contact.by_username_screen import ByUsernameScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC15(BaseTest):
    """
    User has the ability to send friend request by username
    """
    FRIEND = config.PERU_USERNAME

    def test_c15(self):
        log.info("Add contact by username: '{}'".format(self.FRIEND))
        menu = Menu(self.driver)
        by_username = ByUsernameScreen(self.driver)
        menu.go_to(menu.wenums.CONTACTS, [menu.wenums.NEW_CONTACT, menu.wenums.BY_USERNAME], menu.wenums.CONTACTS)
        by_username.search()
        by_username.set_contact_username(self.FRIEND)
        by_username.tap_search()
        by_username.tap_add_contact_btn()

        log.info("Verify friend request sent")
        Verify.true(by_username.request_sent_check(), "No request sent")
