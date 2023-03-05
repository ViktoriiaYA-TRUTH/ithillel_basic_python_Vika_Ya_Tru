def get_max_digit(number):  # returns int
    max_digit = 0
    while number:
        a = number % 10
        max_digit = max(a, max_digit)
        number = number // 10
    return max_digit


def main():
    import random
    number = random.randint(100000000000, 999999999999)
    print(number, get_max_digit(number))


if __name__ == '__main__':
    main()
