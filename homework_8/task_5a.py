def get_max_digit(number):  # returns int
    digits = list(number)
    return max(digits)


def main():
    import random
    number = str(random.randint(100000000000, 999999999999))
    print(number, get_max_digit(number))


if __name__ == '__main__':
    main()



