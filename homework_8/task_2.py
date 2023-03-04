def copydeep(obj):
    if isinstance(obj, list):
        result = []
        for i in obj:
            result.append(copydeep(i))
    elif isinstance(obj, (str, int, float, bool, tuple)):
        result = obj
    return result


def main():
    lst = [1, 2, 3]
    new_lst_copied_deep = copydeep(lst)
    print('The obj: ', lst, '\n', 'Deepcopy:', new_lst_copied_deep, sep='')
    lst.append(777)
    print('The obj: ', lst, '\n', 'Deepcopy:', new_lst_copied_deep, sep='')


if __name__ == '__main__':
    main()
