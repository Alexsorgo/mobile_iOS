from configs import config
from controls.menu import Menu
from screens.search_screens.search_screens import SearchScreen
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC26310(BaseTest):
    """
    User has the ability to search on the chat list screen by part of Group name
    """
    GROUP_NAME = config.GROUP_NAME
    PART_GROUP_NAME = GROUP_NAME[:4]

    def test_c26310(self):
        log.info("Search on the Chat list screen by part of Group name")
        menu = Menu(self.driver)
        search = SearchScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        search.set_search(self.PART_GROUP_NAME)

        log.info("Verify Group Chat is in the search result")
        Verify.true(search.is_result_displayed(self.GROUP_NAME), "Group Chat is not in the search result")
