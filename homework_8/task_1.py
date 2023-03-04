def index(lst, elem=None):
    for idx, item in enumerate(lst):
        if item == elem:
            return idx


def main():
    lst = ['1', 2, 555, 'b', (4, 7)]
    elem = input('Enter an element:')
    print(index(lst, elem))


if __name__ == '__main__':
    main()
