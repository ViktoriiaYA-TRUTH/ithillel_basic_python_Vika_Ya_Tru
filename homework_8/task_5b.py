def get_max_digit(number):  # returns int
    max_digit = 0
    for i in range(12):
        if number % 10 > max_digit:
            max_digit = number % 10
            number = number//10
        else:
            number = number//10
    return max_digit


def main():
    import random
    number = random.randint(100000000000, 999999999999)
    print(number, get_max_digit(number))


if __name__ == '__main__':
    main()
