def triangle_square_and_perimeter(a, b):  # returns 2 values
    s = a * b * 0.5
    p = (a**2 + b**2)**0.5 + a + b
    return s, p


a = int(input('Введіть довжину одного катета:'))
b = int(input('Введіть довжину другого катета:'))
result = triangle_square_and_perimeter(a, b)


print('Площа: ', result[0], '\n',
      'Периметр: ', result[1], sep='')

