store = []
def sort_by_last_letter(string):
    def last_letter(s):
        """
        Just like any other def word, the local
        function is defined at runtime. This will
        result in a new def of last_letter every time
        sort_by_last_letter is called
        :param s:
        :return:
        """
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(string, key=last_letter)


g = 'global'
def outer(p="param"):
    l = "local"
    def inner():
        print(g, p, l)
    inner()


def enclosing():
    x = "closed over"
    def local_func():
        print(x)
    return local_func


def test_enclosing():
    lf = enclosing()
    lf()
    print(lf.__closure__)

def main():
    """Test function"""
    s1 = sort_by_last_letter(["Hello", "from", "ABC"])
    print(s1)
    s2 = sort_by_last_letter(["Hello", "from", "ABC"])
    print(s2)
    s3 = sort_by_last_letter(["Hello", "from", "ABC"])
    print(s3)


if __name__ == '__main__':
    #main()
    #outer()
    test_enclosing()