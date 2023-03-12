import math


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def inside_or_not(self, x_for_dot, y_for_dot):
        d = math.sqrt((x_for_dot - self.x) ** 2 + (y_for_dot - self.y) ** 2)
        if d <= self.radius:
            return True
        else:
            return False


class Dot:
    def __init__(self, x_for_dot, y_for_dot):
        self.x_for_dot = x_for_dot
        self.y_for_dot = y_for_dot


def main():
    a = Circle(4, 4, 16)
    b = Dot(0, 2)
    result = a.inside_or_not(b)
    print(a.inside_or_not(15, 35))


if __name__ == '__main__':
    main()
