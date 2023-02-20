def n_fib(number):
    a, b = 0, 1
    for i in range(number):
        a, b = b, a + b
    return a


def main():
    number = int(input('Введіть натуральне число: '))
    print(n_fib(number))


if __name__ == '__main__':
    main()
