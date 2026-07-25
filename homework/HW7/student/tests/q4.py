OK_FORMAT = True

test = {   'name': 'q4',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> encode('A', 0)\n'A'", 'hidden': False, 'locked': False},
                                   {'code': ">>> encode('AA', 0)\n'AA'", 'hidden': False, 'locked': False},
                                   {'code': ">>> encode('ZABCDEFGHIJKLMNOPQRSTUVWXY', 1)\n'ABCDEFGHIJKLMNOPQRSTUVWXYZ'", 'hidden': False, 'locked': False},
                                   {'code': ">>> encode('A', 27)\n'B'", 'hidden': False, 'locked': False},
                                   {'code': ">>> encode('BUNNY', 17)\n'SLEEP'", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
