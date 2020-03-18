import bert
import paho.mqtt.client as mqtt

from configs import config
from utils.logs import log
from utils.server.base_auth import Auth
from utils.server.parsers import registration_parser

SERVER = config.SERVER
FRIEND_NUMBER = config.AMERICA_COUNTRY_CODE + config.AMERICA_NUMBER
FRIEND_FIRST_NAME = config.AMERICA_FIRSTNAME
FRIEND_LAST_NAME = config.AMERICA_LASTNAME
FRIEND_USER_NAME = config.AMERICA_USERNAME


class Logined(mqtt.Client):

    """User have ability to register new user"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully")

    def on_message(self, client, userdata, msg):
        data = bert.decode(bytes(msg.payload))
        log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        registration_parser.parser(client, msg.payload, FRIEND_FIRST_NAME, FRIEND_LAST_NAME, FRIEND_USER_NAME)

    def run(self, pswa):
        self.will_set(topic=config.PROTOCOL, payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(SERVER, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


def test_25412():
    client_id = "reg_" + FRIEND_NUMBER
    mqtt = Auth(client_id=client_id, clean_session=False)
    _, pswa = mqtt.run(FRIEND_NUMBER)
    client_id = "emqttd_" + FRIEND_NUMBER
    mqtt2 = Logined(client_id=client_id, clean_session=False)
    mqtt2.run(pswa)
