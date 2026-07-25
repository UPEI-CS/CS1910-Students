OK_FORMAT = True

test = {   'name': 'q1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def t1():\n'
                                               '...     pb = {}\n'
                                               "...     ph1 = '902-555-5555'\n"
                                               "...     add_contact(pb, 'andrew', ph1)\n"
                                               "...     ph2 = get_contact(pb, 'andrew')\n"
                                               '...     return ph1 == ph2\n'
                                               '>>> t1()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> def t2():\n'
                                               '...     pb = {}\n'
                                               "...     ph1 = '902-555-5554'\n"
                                               "...     add_contact(pb, 'sally', ph1)\n"
                                               "...     add_contact(pb, 'george', '999-999-9999')\n"
                                               "...     save(pb, 'a.txt')\n"
                                               "...     pb2 = load_contacts('a.txt')\n"
                                               "...     ph2 = get_contact(pb2, 'sally')\n"
                                               '...     return ph1 == ph2\n'
                                               '>>> t2()\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
