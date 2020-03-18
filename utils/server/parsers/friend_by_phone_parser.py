import bert
from erlastic import Atom
from utils.logs import log
from utils.server.models.friend_model import friend
from utils.server.models.search_model import search

global user_id


def parser(client, payload, main_number, friend_phone):
    data = bert.decode(bytes(payload))

    if data[0] == Atom('Profile') and data[8] == 'init':
        roas = (bert.decode(bytes(payload))[3])
        global user_id
        user_id = roas[0][1]
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            search(user_id=user_id, ref='phone', field='phone', type_r=Atom('=='), value=[friend_phone],
                   status=Atom('contact'))), qos=2, retain=False)

    if data[0] == Atom('io') and data[1] == (Atom('ok'), b'phone'):
        if data[2][6]:
            friend_id = data[2][6][0][1]
            my = main_number + '_' + str(user_id)
            log.debug("Add user {} \r\n".format(str(friend_id)))
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                friend(my_id=my, friend_id=friend_id, status=Atom('request'))), qos=2, retain=False)
        if not data[2][6]:
            log.debug('Contact not found')
            log.debug(data)
            client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()
