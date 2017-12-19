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


def main():
    """Test function"""
    s = sort_by_last_letter(["Hello", "from", "ABC"])
    print(s)
    s = sort_by_last_letter(["Hello", "from", "ABC"])
    print(s)
    s = sort_by_last_letter(["Hello", "from", "ABC"])
    print(s)


if __name__ == '__main__':
    main()