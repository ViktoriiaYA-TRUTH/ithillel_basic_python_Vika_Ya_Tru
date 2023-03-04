def index(lst, elem=None):
    for idx, item in enumerate(lst):
        if isinstance(item, int):
            item = str(item)
            if item == elem:
                return idx
        elif isinstance(item, str):
            if item == elem:
                return idx
        elif isinstance(item, tuple):
            elem = tuple(elem)
            return idx
        else:
            return None


def main():
    lst = [1, 2, 555, 'b', (4, 7)]
    elem = input('Enter an element:')
    print(index(lst, elem))


if __name__ == '__main__':
    main()
