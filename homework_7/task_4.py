def sum_symbol_codes(first, last):
    i = range(first, last)
    return sum(i, last)


def main():
    first = int(ord(input('Введіть перший символ: ')))
    last = int(ord(input('Введіть останній символ: ')))
    print(sum_symbol_codes(first, last))


if __name__ == '__main__':
    main()



