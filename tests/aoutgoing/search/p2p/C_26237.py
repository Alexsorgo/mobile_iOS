from configs import config
from controls.menu import Menu
from screens.search_screens.search_screens import SearchScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26237(BaseTest):
    """
    User has the ability to search with case insensitive on the Chats List screen
    """
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c26237(self):
        log.info("Check that search is case insensitive on the Chats List screen")
        menu = Menu(self.driver)
        search = SearchScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        search.set_search(self.FRIEND_NAME.swapcase())

        log.info("Verify Particular P2P Chat is in the search result")
        Verify.true(search.is_result_displayed(self.FRIEND_NAME), "Particular P2P Chat is not in the search result")
