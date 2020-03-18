import bert
from erlastic import Atom
from utils.logs import log
from utils.server.convector import string_to_bytes
from utils.server.exception import InvalidData, PermissionDenied
from utils.server.models.roster_model import roster
from utils.verify import Verify


def parser(client, payload, first_name, last_name, user_name=None):
    data = bert.decode(bytes(payload))
    global userid

    if data[0] == Atom('Profile') and (data[-1]) == Atom('init'):
        roaster = (bert.decode(bytes(payload))[3])
        global user_id
        user_id = roaster[0][1]
        rost = roster(user_id=user_id, first_name=first_name, last_name=last_name, status=Atom('patch'))
        client.publish(topic="events/1//api/anon//", payload=bytearray(rost), qos=2,
                       retain=False)

    elif data[0] == Atom('Roster') and (data[-1]) == Atom('patch'):
        log.debug(user_id)
        log.debug(user_name)
        rost = roster(user_id=user_id, my_username=user_name, status=Atom('nick'))
        log.debug(rost)
        client.publish(topic="events/1//api/anon//", payload=bytearray(rost), qos=2, retain=False)

    elif user_name and data[0] == Atom('Roster') and (data[-1]) == Atom('nick'):
        log.info("Verify roster/nick updated")
        Verify.true(data[5] == string_to_bytes(user_name), 'Username does not set')
        client.disconnect()

    elif data[0] == Atom('Roster') and (data[-1]) == Atom('patch') and user_name is None:
        log.info("Verify user register")
        Verify.true(data[2] == string_to_bytes(first_name), 'First Name doesnt update')
        client.disconnect()

    elif data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise InvalidData("Invalid data response")

    elif data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise PermissionDenied("No permission")
