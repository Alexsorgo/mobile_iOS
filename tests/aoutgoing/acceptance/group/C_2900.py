from configs import config
from screens.chats.camera_screen import CameraScreen
from screens.group.create_group_screen import CreateGroupScreen
from screens.group.group_screen import GroupScreen
from controls.menu import Menu
from tests.aoutgoing.base_test import BaseTest
from utils.helpers.data_generation import magic
from utils.logs import log
from utils.verify import Verify


class TestC2900(BaseTest):
    """
    User has the ability to create group with avatar from camera
    """
    GROUP_NAME = magic.get_word
    FRIEND = config.AMERICA_FIRSTNAME + ' ' + config.AMERICA_LASTNAME

    def test_c2900(self):
        log.info("Create group chat with avatar from camera")
        menu = Menu(self.driver)
        group = GroupScreen(self.driver)
        camera = CameraScreen(self.driver)
        g_create = CreateGroupScreen(self.driver)
        menu.go_to(menu.wenums.GROUPS, [menu.wenums.NEW_GROUP])
        group.add_user(self.FRIEND)
        group.tap_done()
        group.tap_group_name()
        group.set_group_name(self.GROUP_NAME)
        group.tap_save()
        g_create.set_group_avatar()
        g_create.tap_photo_form_camera()
        camera.tap_take_photo()
        camera.tap_accept_photo()
        group.tap_create()
        group.is_group_created()

        log.info("Verify group created with avatar")
        Verify.true(g_create.is_avatar_loaded(), "Avatar doesn't displayed")
