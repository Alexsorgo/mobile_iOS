import bert

from erlastic import Atom


def get_profile():
    module = Atom('Profile')
    phone_id = '12566018988'
    settings = []
    status = Atom('get')

    request_f = (module,phone_id,settings,settings,settings,settings,settings,settings,status)
    request = bert.encode(request_f)
    print('='*5 + 'REQUEST' + '='*5 + '\r\n'+ str(request_f)+'\r\n')
    return request
