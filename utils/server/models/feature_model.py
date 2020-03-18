from erlastic import Atom


def feature(**data):
    module = Atom('Feature')
    expected = ['id', 'key', 'value', 'group']
    actual = data
    my_dict = {}
    for i in expected:
        if i in actual.keys():
            my_dict.update({i: actual[i]})
        else:
            my_dict.update({i: []})

    request_f = (module, my_dict['id'], my_dict['key'], my_dict['value'], my_dict['group'])

    return request_f
