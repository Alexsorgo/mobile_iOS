import paho.mqtt.client as mqtt

import bert
from configs import config
from utils.logs import log
from utils.server.base_auth import Auth
from utils.server.parsers import send_message_parser

FRIEND_NUMBER = config.CHINA_COUNTRY_CODE + config.CHINA_NUMBER
SERVER = config.SERVER
MAIN_NUMBER = config.AMERICA_COUNTRY_CODE + config.AMERICA_NUMBER


class Logined(mqtt.Client):

    """User have ability to send voice message in p2p chat"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully")

    def on_message(self, client, userdata, msg):
        data = bert.decode(bytes(msg.payload))
        log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        send_message_parser.parser(self.chat_type, client, msg.payload, MAIN_NUMBER, FRIEND_NUMBER, self.mime,
                                   self.message_type, self.message_text)

    def run(self, pswa, chat_type, mime, message_type, message_text):
        self.chat_type = chat_type
        self.mime = mime
        self.message_type = message_type
        self.message_text = message_text
        self.will_set(topic=config.PROTOCOL, payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(SERVER, 1883, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        return rc


def incoming_message(chat_type, mime, message_type=None, message_text=None):
    client_id = "reg_" + MAIN_NUMBER
    mqtt_client = Auth(client_id=client_id, clean_session=False)
    _, pswa = mqtt_client.run(MAIN_NUMBER)
    client_id = "emqttd_" + MAIN_NUMBER
    mqtt2 = Logined(client_id=client_id, clean_session=False)
    mqtt2.run(pswa, chat_type, mime, message_type, message_text)
