import time

import bert
from erlastic import Atom
from utils.logs import log
from utils.server.convector import string_to_bytes
from utils.server.exception import InvalidData, PermissionDenied
from utils.server.models.feature_model import feature
from utils.server.models.job import act, job
from utils.server.models.send_msg import send_message
from utils.verify import Verify


def parser(chat_type, client, payload, main_number, friend_number, mime, message_type=None):
    data = bert.decode(bytes(payload))
    global main_id
    global friend_id
    global p2p_chat
    global group_chat
    global message_id
    global member_id
    global group_friend_id

    if data[0] == Atom("Profile"):
        for field in data[3][0][6]:
            if field[-1] == Atom('friend'):
                if field[8]:
                    p2p_chat = field[8][3]

        group_chat = data[3][0][7][-1][7][0][3]
        group_friend_id = data[3][0][7][-1][1]

        if chat_type == 'p2p' or chat_type == 'myself':
            for field in data[3][0][6]:
                if field[-1] == Atom('friend'):
                    if field[1].split(b'_')[0] == string_to_bytes(main_number):
                        log.debug('Main profile found')
                        main_id = field[1]
                        if chat_type == 'myself':
                            friend_id = main_id
                            message_id = field[8][1]
                            p2p_chat = field[8][3]
                        if chat_type == 'p2p':
                            if field[0] == Atom('Contact') and field[-1] == Atom('friend') and \
                                    field[1].split(b'_')[0] == string_to_bytes(friend_number):
                                friend_id = field[1]
                                if field[8]:
                                    message_id = field[8][1]
                                    p2p_chat = field[8][3]

            feature_model = feature(id='Autotest_feature_id' + str(time.time()).split('.')[0], key='TimeZone',
                                    value='Europe/Kiev', group='JOB_TIMEZONE')
            message_model = bert.decode(send_message(main_id, friend_id, p2p_chat, mime, data[1], message_type))
            act_model = act(name='publish', data=main_id)
            time_plus_ten_min = (int(str(time.time()).split('.')[0]) + 6000) * 1000
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                job(feed_id=act_model, time=time_plus_ten_min, data=[message_model],
                    settings=feature_model, status=Atom('init'))), qos=2, retain=False)

        if chat_type == 'group':
            for field in data[3][0][6]:
                if field[-1] == Atom('friend'):
                    if field[1].split(b'_')[0] == string_to_bytes(main_number):
                        log.debug('Main profile found')
                        main_id = field[1]

            message_id = data[3][0][7][-1][15][1]
            friend_id = data[3][0][7][-1][1]
            member_id = data[3][0][7][-1][7][0][1]

            log.debug('Send job')
            feature_model = feature(id='Autotest_feature_id'+str(time.time()).split('.')[0], key='TimeZone',
                                    value='Europe/Kiev', group='JOB_TIMEZONE')
            message_model = bert.decode(send_message(main_id, group_friend_id, group_chat, mime, data[1], message_type))

            act_model = act(name='publish', data=main_id)
            time_plus_ten_min = (int(str(time.time()).split('.')[0])+600)*1000
            client.publish(topic="events/1//api/anon//", payload=bytearray(
                job(feed_id=act_model, time=time_plus_ten_min, data=[message_model],
                    settings=feature_model, status=Atom('init'))), qos=2, retain=False)

    elif data[0] == Atom('Job') and data[-1] == Atom('pending'):
        log.debug('Verify job go to pending')
        Verify.true(data[0] == Atom('Job') and data[-1] == Atom('pending'), 'Job not in pending')
        client.disconnect()

    elif data == (Atom('io'), (Atom('error'), Atom('invalid_data')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise InvalidData("Invalid data response")

    if data == (Atom('io'), (Atom('error'), Atom('permission_denied')), b''):
        log.error("Something going wrong")
        client.disconnect()
        raise PermissionDenied("No permission")
