class Reader:
    def __init__(self, filename):
        self._filename = filename
        self._f = open(self._filename, mode='rt', encoding='utf-8')

    def close(self):
        self._f.close()

    def read(self):
        return self._f.read()