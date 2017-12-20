class Point2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return '({}, {})'.format(self._x, self._y)

    def __repr__(self):
        return "Point2D(x={}, y={})".format(self._x, self._y)

    def __format__(self, format_spec):
        return "Formatted point: {}, {}, {}".format(
            self._x, self._y, format_spec)


if __name__ == '__main__':
    print("This is a point {}".format(Point2D(2, 4)))
    # p1 = Point2D(5, 7)
    # print(p1)
    # print(str(p1))
    # print(repr(p1))
    # # What about if I have a collection of objects
    # l = [Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=3)]
    # print(l)
    # print(repr(l))
    # # What about a dict
    # d = {i:Point2D(x=0, y=0) for i in range(3)}
    # print(repr(d))

