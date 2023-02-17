import math


def cone_square_and_volume(radius, height):  # returns 2 floats
    s = math.pi * radius * math.sqrt(radius**2 + height**2) + math.pi * radius**2
    v = math.pi * radius**2 * height / 3
    return s, v


radius = int(input('Введіть радіус: '))
height = int(input('Введіть висоту конуса: '))

print(cone_square_and_volume(radius, height))
