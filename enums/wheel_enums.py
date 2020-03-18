# First level items
from configs import config

ACTIONS = "Actions"
CALLS = "Calls"
CHANNELS = "Channels"
CHATS = "Chats"
CONTACTS = "Contacts"
GROUPS = "Groups"
HOME = "Home"
MYSELF = "Myself"
SEARCH = "Search"
SETTINGS = "Settings"

FIRST_LVL_ITEM_LIST = [CALLS, SETTINGS, HOME, SEARCH, MYSELF, ACTIONS, CHATS, GROUPS, CONTACTS, CHANNELS]


# Second level items
ALL = "All"
BUILD_NUMBER = "Build number"
BY_CONTACTS = "By Contacts"
BY_NUMBER = "By Number"
BY_QR_CODE = "By QR Code"
BY_USERNAME = "By Username"
CAMERA = "Camera"
CHANGE_NUMBER = "Change Number"
CONTACT = "Contact"
DATA_AND_STORAGE = "Data and Storage"
EDIT_PROFILE = "Edit Profile"
FAMILY = "Family"
FILE = "File"
FRIENDS = "Friends"
GALLERY = "Gallery"

HISTORY = "History"
INVITE_FRIENDS = "Invite Friends"
LANGUAGE = "Language"
LOCATION = "Location"
TRANSFER = "Transfer"
CHAT_OPTIONS = "Chat Options"
CALL = "Call"
GROUP_OPTIONS = 'Group Options'
LOG_OUT = "Log Out"
DELETE_ACCOUNT = "Delete Account"
MEDIA = "Media"
MY_CHANNELS = "My Channels"
MY_NAME = "My Name"
MY_PHOTO = "My Photo"
MY_QR_CODE = "My QR Code"
MY_USERNAME = "My Username"
NEW_CHANNEL = "New Channel"
NEW_CHAT = "New Chat"
NEW_GROUP = "New Group"
NEW_CONTACT = "New Contact"
NOTIFICATIONS = "Notifications"
PRIVACY = "Privacy"

RECENTS = "Recents"
SECURITY = "Security"
SEND_LOCATION = "Send Location"
STARRED = "Starred"
SUPPORT = "Support"
THEME = "Theme"
WHEEL_POSITION = "Wheel position"
WORK = "Work"

GO_TO_GALLERY = "Go to gallery"


CHANNELS_LVL_ITEM_LIST = [ALL, RECENTS, MY_CHANNELS, NEW_CHANNEL]

CHAT_ACTIONS_LVL_ITEM_LIST = [GROUP_OPTIONS, CHAT_OPTIONS, TRANSFER, LOCATION, CONTACT, CALL, MEDIA, CAMERA]

CHATS_LVL_ITEM_LIST = [FAMILY, FRIENDS, WORK, ALL, RECENTS, STARRED, NEW_CHAT]

CONTACTS_LVL_ITEM_LIST = [INVITE_FRIENDS, BY_CONTACTS, BY_QR_CODE, BY_NUMBER, BY_USERNAME, NEW_CONTACT, ALL, HISTORY]

GROUPS_LVL_ITEM_LIST = [FAMILY, FRIENDS, WORK, ALL, RECENTS, STARRED, NEW_GROUP]

HOME_ACTIONS_LVL_ITEM_LIST = [MY_QR_CODE, MY_PHOTO, MY_USERNAME, CHANGE_NUMBER, MY_NAME, EDIT_PROFILE]

if config.BUNDLE_ID == 'com.nynja.dev.mobile.communicator':
    SETTINGS_LVL_ITEM_LIST = [LOG_OUT, NOTIFICATIONS, CHANGE_NUMBER, WHEEL_POSITION, BUILD_NUMBER,
                              SUPPORT, LANGUAGE, THEME, DATA_AND_STORAGE, SECURITY, PRIVACY]
else:
    SETTINGS_LVL_ITEM_LIST = [LOG_OUT, NOTIFICATIONS, CHANGE_NUMBER, WHEEL_POSITION, BUILD_NUMBER,
                              SUPPORT, LANGUAGE, THEME, DATA_AND_STORAGE, SECURITY, PRIVACY]

# TODO: Not implemented yet
# Calls level items
CALLS_LVL_ITEM_LIST = []

# Helper
SECOND_LVL_MANAGER = {CALLS: CALLS_LVL_ITEM_LIST,
                      SETTINGS: SETTINGS_LVL_ITEM_LIST,
                      CHATS: CHAT_ACTIONS_LVL_ITEM_LIST,
                      GROUPS: GROUPS_LVL_ITEM_LIST,
                      CHANNELS: CHANNELS_LVL_ITEM_LIST,
                      CONTACTS: CONTACTS_LVL_ITEM_LIST,
                      ACTIONS: {HOME: HOME_ACTIONS_LVL_ITEM_LIST,
                                CHATS: CHAT_ACTIONS_LVL_ITEM_LIST}}

# Not existed item for the third level wheel
THIRD_LVL_ITEM_LIST = ["Some item"]
