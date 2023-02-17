import math


def circles_intersect(x1, y1, r1, x2, y2, r2): # returns boolean value
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return d


def main():
    x1 = int(input('Enter x1'))
    y1 = int(input('Enter y1'))
    r1 = int(input('Enter r1'))
    x2 = int(input('Enter x2'))
    y2 = int(input('Enter y2'))
    r2 = int(input('Enter r2'))
    if circles_intersect(x1, y1, r1, x2, y2, r2) > r1 + r2:
        print('Перетинаються')
    else:
        print('Не перетинаються')


if __name__ == '__main__':
    main()
