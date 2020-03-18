from selenium.common.exceptions import NoSuchElementException

from configs import config
from model.element import Element
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen
from utils.helpers.manage_users import Manager
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC17(BaseTest):
    """
    User has the ability to accept friend request
    """
    PHONE_NUMBER = config.AMERICA_NUMBER
    COUNTRY_CODE = config.AMERICA_COUNTRY_CODE

    def test_c17(self):
        log.info("Accept friend request from : '{}'".format(config.CHINA_NUMBER))
        manage = Manager(self.driver)
        manage.log_out()
        nynja_login_screen = LoginScreen(self.driver)
        nynja_home_screen = HomeScreen(self.driver)

        nynja_login_screen.set_full_number(self.COUNTRY_CODE, self.PHONE_NUMBER)
        nynja_login_screen.tap_confirm_btn()
        nynja_login_screen.set_sms()

        log.info("Authorised by friend: '{}'".format(self.PHONE_NUMBER))

        Verify.true(nynja_home_screen.is_home_screen_displayed(), "Home Screen is not displayed")

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

