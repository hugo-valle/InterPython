import socket
from pprint import pprint as pp


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


def sequence_class(immutable):
    return tuple if immutable else list


def test_sequence_class():
    seq = sequence_class(immutable=True)
    t = seq("Weber State")
    print(t)


def test_lambda():
    scientists = ["Marie Curie French",
                  "Nicolas Bohr Germany",
                  "Issac Newton England",
                  "Dimitri Mendelev Rusia",
                  "Charles Darwing UK",
                  "Alber Einstein Germany"]

    # Print list sorted by last name
    # use a Lambda function
    pp(sorted(scientists, key=lambda name: name.split()[-2]))

    # Task sort the array by country member string[2]


if __name__ == '__main__':
    #test_sequence_class()
    test_lambda()
