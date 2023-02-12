import math


def degrees2radians(degrees):  # returns float: radians val
    return math.pi * degrees / 180


print(math.cos(degrees2radians(45)), '\n',
      math.cos(degrees2radians(60)), '\n',
      math.cos(degrees2radians(40)))



