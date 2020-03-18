import bert
import paho.mqtt.client as mqtt

from configs import config
from utils.logs import log
from utils.server.base_auth import Auth
from utils.server.parsers import delete

MAIN_NUMBER = config.CHINA_COUNTRY_CODE + config.CHINA_NUMBER
SERVER = config.SERVER


class Logined(mqtt.Client):

    """User have ability to search another user by phone number"""

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            log.info("Reconnected successfully \r\n")

    def on_message(self, client, userdata, msg):
        data = bert.decode(bytes(msg.payload))
        log.info('='*5 + 'RESPONSE' + '='*5 + '\r\n'+ str(data) + '\r\n')
        delete.parser(client, msg.payload, MAIN_NUMBER)

    def run(self, pswa):
        self.will_set(topic=config.PROTOCOL, payload=None, qos=2, retain=False)
        self.username_pw_set(username="api", password=pswa)
        self.connect(SERVER, 8443, 60)

        rc = 0
        while rc == 0:
            rc = self.loop()

        print(rc)
        return rc


def test_delete_main():
    client_id = "reg_" + MAIN_NUMBER
    mqtt_client = Auth(client_id=client_id, clean_session=False)
    _, pswa = mqtt_client.run(MAIN_NUMBER)
    client_id = "emqttd_" + MAIN_NUMBER
    mqtt2 = Logined(client_id=client_id, clean_session=False)
    mqtt2.run(pswa)
