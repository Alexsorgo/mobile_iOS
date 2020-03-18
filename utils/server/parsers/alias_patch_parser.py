import bert
from erlastic import Atom
from utils.logs import log
from utils.server.convector import string_to_bytes
from utils.server.exception import InvalidData, PermissionDenied
from utils.server.models.member import member
from utils.verify import Verify


def parser(client, payload, new_alias):
    data = bert.decode(bytes(payload))
    global room_id
    global member_id

    if data[0] == Atom("Profile"):
        for field in data:
            if field and list == type(field):
                for room in field[0]:
                    if room and list == type(room) and room[0][0] == Atom('Room'):
                        for member_field in room[-1]:
                            if member_field and list == type(member_field) and tuple == type(member_field[0]) \
                                    and member_field[0][0] == Atom('Member'):
                                global member_id
                                member_id = member_field[0][1]

        client.publish(topic="events/1//api/anon//", payload=bytearray(
            member(member_id=member_id, container=Atom('chain'), alias=new_alias, status=Atom('patch'))), qos=2,
                       retain=False)

    if data[0] == Atom('Member'):
        log.debug('Verify member patched')
        Verify.equals(string_to_bytes(new_alias), data[11], 'Not new alias')
        client.disconnect()

    if data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise InvalidData("Invalid data response")

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise PermissionDenied("No permission")
