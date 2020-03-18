from configs import config
from controls.menu import Menu
from screens.search_screens.search_screens import SearchScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26307(BaseTest):
    """
    User has the ability to search on the group list screen
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c26307(self):
        log.info("Search on the group list screen")
        menu = Menu(self.driver)
        search = SearchScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        search.set_search(self.GROUP_NAME)

        log.info("Verify group chat is in the search result")
        Verify.true(search.is_result_displayed(self.GROUP_NAME), "Group Chat is not in the search result")
