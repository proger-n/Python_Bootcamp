import re


def fix_wiring(plugs: list, sockets: list, cables: list):
    return map(lambda x: f'plug {x[2]} into {x[1]} using {x[0]}' if x[0] != 'weld' else f'weld {x[2]} to {x[1]} without plug',
               zip(map(lambda s: s if isinstance(s, str) and re.match(r'plug\S', s) else 'weld', filter(
                       lambda s: isinstance(s, str), plugs)), filter(lambda s: re.match(r'socket\S', s), filter(
                           lambda s: isinstance(s, str), sockets)), filter(lambda s: re.match(r'cable\S', s), filter(
                               lambda s: isinstance(s, str), cables))))


def tests():

    plugs = ['plug1', 'plug2', 'plug3', 'pl']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    print("TEST 0:")
    print("INPUT 0:")
    print("plugs=", plugs)
    print("sockets=", sockets)
    print("cables=", cables)
    print("OUTPUT 0:")
    for c in fix_wiring(plugs, sockets, cables):
        print(c)
    print("----------------------------------------")

    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    print("TEST 1:")
    print("INPUT 1:")
    print("plugs=", plugs)
    print("sockets=", sockets)
    print("cables=", cables)
    print("OUTPUT 1:")
    for c in fix_wiring(plugs, sockets, cables):
        print(c)
    print("----------------------------------------")


if __name__ == "__main__":
    tests()
