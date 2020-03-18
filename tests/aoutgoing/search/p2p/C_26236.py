from configs import config
from controls.menu import Menu
from screens.search_screens.search_screens import SearchScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26236(BaseTest):
    """
    User has the ability to search on the chat list screen
    """
    FRIEND_NAME = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c26236(self):
        log.info("Search on the Chat list screen")
        menu = Menu(self.driver)
        search = SearchScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        search.set_search(self.FRIEND_NAME)

        log.info("Verify Particular P2P Chat is in the search result")
        Verify.true(search.is_result_displayed(self.FRIEND_NAME), "Particular P2P Chat is not in the search result")
