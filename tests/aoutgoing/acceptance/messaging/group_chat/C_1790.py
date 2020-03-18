from configs import config
from screens.group.group_list_screen import GroupListScreen
from screens.chats.camera_screen import CameraScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.logs import log
from utils.verify import Verify


class TestC1790(BaseTest):
    """
    User has the ability to send camera photo message in group chat
    """
    GROUP_NAME = config.GROUP_NAME

    def test_c1790(self):
        log.info("Send camera photo message in group chat")
        menu = Menu(self.driver)
        group_list = GroupListScreen(self.driver)
        camera = CameraScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.ALL])
        group_list.open_group_chat(self.GROUP_NAME)
        menu.go_to(menu.wenums.ACTIONS, [menu.wenums.CAMERA], menu.wenums.CHATS)
        camera.tap_take_photo()
        camera.tap_send_button()

        log.info("Verify camera photo message displayed")
        Verify.true(camera.is_image_displayed(), "No sent camera shot message in list")
