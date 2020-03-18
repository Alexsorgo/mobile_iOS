# -*- coding: utf-8 -*-
# Constants file

APPIUM_SERVER_URL = "http://127.0.0.1:4723/wd/hub"
PLATFORM_NAME = 'ios'  # either "Android" or "iOS"
# PLATFORM_VERSION = '7.1.2'
# DEVICE_NAME = 'Nexus 5X'
# PLATFORM_VERSION = '10.3.3'
PLATFORM_VERSION = '11.3.1'
# PLATFORM_VERSION = '11.2.1'
# PLATFORM_VERSION = '12.0'
# DEVICE_NAME = 'iPhone6'
DEVICE_NAME = 'Tec’s iPhone'
# DEVICE_NAME = 'sorgo’s iPhone'
# DEVICE_NAME = 'iPhone (Tec)'
# UDID = '00bf1683ec8c4194969b60cbc40fa06772d64249'
UDID = '5bf6c17a74974c016f3aa73d911d43e52f908c48'
# UDID = '46d80597f089a4a87a5a1eabbdf2f52991461047'
# UDID = '504f50605e2a0a67aa6ec862c2f4d0f42910c711'
BUNDLE_ID = 'com.nynja.mobile.communicator'
PASSWORD = '272b9acb0aaf1902c8b826de040ffabdf7cda8ca3f8355b0d117075c88a1c0d3ce7b3437718d1cbf54b5e5a996b1d6d749964671' \
           'da49c9b20631ef7dc592a19c25369c6dbcccdc1a33944e18687eb801f74ff4775893edd5368f0037674feb70'
MY_NUMBER = '8613151713157' # china
if BUNDLE_ID == 'com.nynja.rc.mobile.communicator':
    SERVER = '35.198.110.223'  # pre-prod
elif BUNDLE_ID == 'com.nynja.dev.mobile.communicator':
    SERVER = '54.201.154.141' # dev
elif BUNDLE_ID == 'com.nynja.mobile.communicator':
    # SERVER = '35.230.49.68'  # prod
    SERVER = 'im-fallback.nynja.net'

PROTOCOL = 'version/10'


# USERS:
# User for test: main actions
CHINA_COUNTRY_CODE = "86"
CHINA_NUMBER = "13777322455"
CHINA_FIRSTNAME = "China"
CHINA_LASTNAME = "Autotest"
CHINA_USERNAME = "CH"

# User for test: friend request by phone number, p2p chat and group chat
AMERICA_COUNTRY_CODE = '1'
AMERICA_NUMBER = '2566018988'
AMERICA_FIRSTNAME = 'America'
AMERICA_LASTNAME = 'Autotest'
AMERICA_USERNAME = 'US'

# User for test: friend request by username
PERU_COUNTRY_CODE = '51'
PERU_NUMBER = '997259024'
PERU_FIRSTNAME = 'Peru'
PERU_LASTNAME = 'Autotest'
PERU_USERNAME = 'PE'

# User for test: friend request by contacts
UKRAINE_COUNTRY_CODE = '380'
UKRAINE_NUMBER = '998681837'
UKRAINE_FIRSTNAME = 'Ukraine'
UKRAINE_LASTNAME = 'Autotest'
UKRAINE_USERNAME = 'UA'


NOTALLOWED_LOGIN = '2568386768'
INCORRECT_LOGIN = '1111111111'
FAKE_SMS = '903182'
INCORRECT_FIRSTNAME = 'QWERTYUIOPASDFGHJKLZXCVBNMQWERTYUI'
DELETE_MESSAGE = 'Deleted'
STARED_MESSAGE = 'Star'
GROUP_NAME = 'Chainsmokers'
CHANNEL_NAME = 'Market'
MAX_GROUP_NAME = 'qwertyuiopasdfghjklzxcvbnmqwertyuio'
