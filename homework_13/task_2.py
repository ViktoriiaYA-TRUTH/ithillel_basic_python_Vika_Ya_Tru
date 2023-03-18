import math


class Circle:
    """Class defines the coordinates for center of a circle and radius of a circle"""
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def inside_or_not(self, point):
        """If point is inside a circle def inside_or_not returns True and if not - False"""
        d = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        return d <= self.radius


class Point:
    """Defines coordinates of a point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    """Defines is the point inside a circle or not with actual parameters"""
    a = Circle(4, 4, 16)
    b = Point(18, 12)
    result = a.inside_or_not(b)
    print(result)


if __name__ == '__main__':
    main()
