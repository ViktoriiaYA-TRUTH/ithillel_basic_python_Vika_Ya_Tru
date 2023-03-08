def lchain(*iterables): # returns list
    lst = []
    for i in iterables:
        lst.extend(i)
    return lst


def main():
    print(lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))


if __name__ == '__main__':
    main()

