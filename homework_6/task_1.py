def is_even(number): # returns boolean value
    return number % 2 == 0


def main():
    number = int(input('Enter a number: '))
    if is_even(number):
        print('even')
    else:
        print('odd')


if __name__ == '__main__':
    main()
