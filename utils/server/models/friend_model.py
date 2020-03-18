import bert

from erlastic import Atom


def friend(**data):
    module = Atom('Friend')
    expected = ['my_id', 'friend_id', 'settings', 'status']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['my_id'], my_dict['friend_id'], my_dict['settings'], my_dict['status'])

    by_phone = bert.encode(request_f)
    return by_phone
