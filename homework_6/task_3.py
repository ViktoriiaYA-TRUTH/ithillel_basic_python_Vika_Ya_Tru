import cmath


def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)
    if discriminant > 0:
        return x1, x2
    elif discriminant == 0:
        return x1, x2
    else:
        return complex(x1), complex(x2)


def main():
    a = int(input('Введіть значення а: '))
    b = int(input('Введіть значення b: '))
    c = int(input('Введіть значення c: '))
    if a == 0:
        print('Значення а не може дорівнювати 0')
    else:
        print(solve_quadratic_equation(a, b, c))


if __name__ == '__main__':
    main()
