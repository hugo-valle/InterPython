"""
Python Review of classes
"""
import math


class MyFirstClass:
    pass


class Point:
    """
    Represents a point in a 2-D geometric coordinates
    """
    def __init__(self, x=0, y=0):
        """
        Initializes the position of a new point.
         If they are not specified, the point defaults
         to the origin
        :param x: x coordinate. Default = 0
        :param y: y coordinate. Default = 0
        """
        self._x = x
        self._y = y

    # Add some instance methods: Do something
    def reset(self):
        """
        Reset the point to the origin location in 2D Space
        :return: Nothing
        """
        self._x = 0
        self._y = 0

    def get_point(self):
        """
        Get current x and y coordinate values of the 2D point
        :return:
        """
        return self._x, self._y

    def set_point(self, x, y):
        """
        Move point to a new location in a 2D space
        :param x: x coordinate
        :param y: y coordinate
        :return: nothing
        """
        self._x = x
        self._y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second
        point passed as a parameter.
        This method uses Pythagorean Theorem to calculate
        the distance between two points
        :param other_point: second point to calculate
        :return: Distance between two points (float)
        """
        return math.sqrt(
            (self._x - other_point._x)**2 +
            (self._y - other_point._y)**2)


def main():
    p1 = Point() # take default
    p2 = Point(2, 5) # set values
    # Add information
    # p1.x = 5
    # p1.y = 4
    # p2.x = 3
    # p2.y = 6
    print(p1._x, p1._y)
    #p1.reset()
    print(p2._x, p2._y)
    print(p2.calculate_distance(p1))
    p1.set_point(3, 2)
    print(p1.get_point())
    print(p2.get_point())
    print(p2.calculate_distance(p1))


if __name__ == '__main__':
    main()