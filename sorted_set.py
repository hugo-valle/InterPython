class SortedSet:
    def __init__(self, items = None):
        """
        Sorted returns a list, regardless of
        which iterable object you passed.
        """
        self._items = sorted(set(items)) \
            if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)