from configs import config
from screens.add_contact.by_number_screen import ByNumberScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC14(BaseTest):
    """
    User has the ability to send friend request by phone number
    """
    COUNTRY_CODE = config.AMERICA_COUNTRY_CODE
    PHONE_NUMBER = config.AMERICA_NUMBER

    def test_c14(self):
        log.info("Add contact by number: '{}'".format(config.AMERICA_NUMBER))
        menu = Menu(self.driver)
        by_number = ByNumberScreen(self.driver)
        menu.go_to(menu.wenums.CONTACTS, [menu.wenums.NEW_CONTACT, menu.wenums.BY_NUMBER], menu.wenums.CONTACTS)
        by_number.search()
        by_number.set_contact_number(self.COUNTRY_CODE, self.PHONE_NUMBER)
        by_number.tap_search()
        by_number.tap_add_contact_btn()

        log.info("Verify friend request sent")
        Verify.true(by_number.request_sent_check(), "No request sent")
