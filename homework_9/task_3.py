def copydeep(obj):
    if isinstance(obj, list):
        result = []
        for i in obj:
            result.append(copydeep(i))
    elif isinstance(obj, tuple):
        result = list()
        for i in obj:
            result.append(copydeep(i))
        return tuple(result)
    elif isinstance(obj, (str, int, float, bool)):
        result = obj

    elif isinstance(obj, dict):
        result = {
            copydeep(key): copydeep(obj)
            for key, obj in obj.items()
        }
    return result


def main():
    tuple_example = (1, 67, 49)
    new_tuple = copydeep(tuple_example)
    changed_tuple = new_tuple + (99, 101)
    print(tuple_example, new_tuple, changed_tuple)

    my_dict = {1: 'm', 66: 'yy'}
    new_dict_copied_deep = copydeep(my_dict)
    print('The obj: ', my_dict, 'Deepcopy:', new_dict_copied_deep)
    new_dict_copied_deep.update({777: 'iii'})
    print('The obj: ', my_dict, 'Deepcopy:', new_dict_copied_deep)


if __name__ == '__main__':
    main()
