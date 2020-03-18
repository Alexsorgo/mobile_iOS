from controls.menu import Menu
from screens.search_screens.search_screens import SearchScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26309(BaseTest):
    """
    User has the ability to hint about empty search result on the group list screen
    """
    INVALID_GROUP_NAME = magic.get_text_message

    def test_c26309(self):
        log.info("Hint about empty search result on the group list screen")
        menu = Menu(self.driver)
        search = SearchScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        search.set_search(self.INVALID_GROUP_NAME)

        log.info("Verify Hint about empty search result is shown")
        Verify.true(search.is_no_result_displayed(), "Hint about empty search result is not shown")
