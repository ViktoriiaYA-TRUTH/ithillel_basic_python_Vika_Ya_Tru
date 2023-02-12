import math


def degrees2radians(degrees):  # returns float: radians value
    return (180/math.pi) * degrees


print(math.cos(degrees2radians(45)), '\n',
      math.cos(degrees2radians(60)), '\n',
      math.cos(degrees2radians(40)))



