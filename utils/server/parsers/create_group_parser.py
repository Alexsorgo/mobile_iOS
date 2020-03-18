import bert
from erlastic import Atom
from utils.logs import log
from utils.server.convector import string_to_bytes
from utils.server.exception import InvalidData, PermissionDenied
from utils.server.models.create_group import create_group
from utils.verify import Verify


def parser(client, payload, main_number, friend_phone, avatar=False, alias_check=False):
    data = bert.decode(bytes(payload))
    global user_id
    global main_first_name
    global main_last_name

    if data[0] == Atom('Profile') and data[8] == 'init':
        contacts = data[3][0][6]
        for field in contacts:
            if field[0] == Atom('Contact') and field[1].split(b'_')[0] == string_to_bytes(main_number):
                log.debug('Main profile found')
                user_id = main_id = field[1]
                main_first_name = field[3]
                main_last_name = field[4]
                main_alias = []
                if field[5]:
                    main_alias = field[5]
            if field[0] == Atom('Contact') and field[-1] == Atom('friend') and \
                    field[1].split(b'_')[0] == string_to_bytes(friend_phone):
                friend_id = field[1]
                friend_first_name = field[3]
                friend_last_name = field[4]
                friend_alias = []
                if field[5]:
                    friend_alias = field[5]
        client.publish(topic="events/1//api/anon//", payload=bytearray(
            create_group(main_id, main_first_name, main_last_name, main_alias, friend_id,
                         friend_first_name, friend_last_name, friend_alias, avatar)), qos=2, retain=False)

    if data[0] == Atom('Room') and alias_check:
        log.info('Verify group created and alias exist')
        Verify.true((data[15][10][0][3] == user_id + b' created the group' and
                     ([field[0][11] for field in data if field and list == type(field) and int != type(field[0]) and
                       field[0][-1] == Atom("admin")][0] == main_first_name + main_last_name)),
                    "No message about creation")
        client.disconnect()

    elif data[0] == Atom('Room'):
        log.info("Verify group creation")
        Verify.true((data[15][10][0][3] == user_id + b' created the group' and
                     (data[8] != [] if avatar else True)), "No message about creation")
        client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise InvalidData("Invalid data response")

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise PermissionDenied("No permission")
