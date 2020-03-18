from selenium.common.exceptions import NoSuchElementException

from configs import config
from model.element import Element
from screens.add_contact.by_contacts_screen import ByContactsScreen
from screens.home_screen import HomeScreen
from screens.login_screen import LoginScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.manage_users import Manager
from utils.logs import log
from utils.verify import Verify


class TestC16(BaseTest):
    """
    User has the ability to send friend request by phone book
    """
    FRIEND = config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME
    PHONE_NUMBER = config.UKRAINE_NUMBER
    COUNTRY_CODE = config.UKRAINE_COUNTRY_CODE

    def test_c16(self):
        log.info("Add contact by contact book: '{}'".format(config.UKRAINE_FIRSTNAME + ' ' + config.UKRAINE_LASTNAME))
        contacts = ByContactsScreen(self.driver)
        menu = Menu(self.driver)
        menu.go_to(menu.wenums.CONTACTS, [menu.wenums.NEW_CONTACT, menu.wenums.BY_CONTACTS], menu.wenums.CONTACTS)
        contacts.tap_add_contact(self.FRIEND)

        log.info("Verify friend request sent")
        Verify.true(contacts.requested_check(), "No request sent")

        menu.long_press_wheel()
        manage = Manager(self.driver)
        manage.log_out()
        nynja_login_screen = LoginScreen(self.driver)
        nynja_home_screen = HomeScreen(self.driver)

        nynja_login_screen.set_full_number(self.COUNTRY_CODE, self.PHONE_NUMBER)
        nynja_login_screen.tap_confirm_btn()
        nynja_login_screen.set_sms()

        log.info("Authorised by friend: '{}'".format(self.PHONE_NUMBER))

        Verify.true(nynja_home_screen.is_home_screen_displayed(), "Home Screen is not displayed")

        # TODO: Update
        contact = self.driver.find_elements_by_xpath('//XCUIElementTypeCell'
                                                     '[@name="contact_request_profile_contact_cell"]')
        log.info('Contacts cell collected')
        if not contact:
            raise NoSuchElementException
        for elem in contact:
            log.info('We are in elements')
            if elem.find_element_by_xpath('//XCUIElementTypeStaticText').get_attribute('name') == \
                    config.CHINA_FIRSTNAME + ' ' + config.CHINA_LASTNAME:
                log.info('China user find')
                accept_friend = elem.find_element_by_id('Accept')
                el = Element(self.driver)
                el.tap_element(accept_friend)

        manage.log_out()

        nynja_login_screen.set_full_number(config.CHINA_COUNTRY_CODE, config.CHINA_NUMBER)
        nynja_login_screen.tap_confirm_btn()
        nynja_login_screen.set_sms()

        log.info("Authorised by main account: '{}'".format(config.CHINA_NUMBER))

        Verify.true(nynja_home_screen.is_home_screen_displayed(), "Home Screen is not displayed")
