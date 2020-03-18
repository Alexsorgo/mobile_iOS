from controls.menu import Menu
from enums import error_enums
from screens.search_screens.search_screens import SearchScreen
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC26238(BaseTest):
    """
    User has the ability to hint about empty search result on the chat list screen
    """
    INVALID_FRIEND_NAME = magic.get_text_message

    def test_c26238(self):
        log.info("Hint about empty search result on the chat list screen")
        menu = Menu(self.driver)
        search = SearchScreen(self.driver)
        menu.go_to(menu.wenums.CHATS, [menu.wenums.ALL])
        search.set_search(self.INVALID_FRIEND_NAME.swapcase())

        log.info("Verify Hint about empty search result is shown")
        Verify.true(search.error_verify(error_enums.NO_SEARCH_RESULT), "Hint about empty search result is not shown")
