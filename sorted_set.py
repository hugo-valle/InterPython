from bisect import bisect_left

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

    def __iter__(self):
        # Python 3.3 or less
        # for item in self._items:
        #     yield item
        # Python > 3.3
        # yield from self._items
        return iter(self._items)

    def __getitem__(self, index):
        #print("index={}".format(index))
        #print("indexType={}".format(type(index)))
        result = self._items[index]
        return (SortedSet(result)
                if isinstance(index, slice)
                else result)

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items)
            if self._items
            else '' )

    def __eq__(self, rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def count(self, item):
        index = bisect_left(self._items, item)
        found = ((index != len(self._items))
                 and (self._items[index] == item))

        return int(found)

