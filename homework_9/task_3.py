def copydeep(obj):
    if isinstance(obj, list):
        result = []
        for i in obj:
            result.append(copydeep(i))
    elif isinstance(obj, (str, int, float, bool, tuple)):
        result = obj

    elif isinstance(obj, dict):
        result = {
            copydeep(key): copydeep(obj)
            for key, obj in obj.items()
        }
    return result


def main():
    my_dict = {1: 'm', 66: 'yy'}
    new_dict_copied_deep = copydeep(my_dict)
    print('The obj: ', my_dict, 'Deepcopy:', new_dict_copied_deep)
    new_dict_copied_deep.update({777: 'iii'})
    print('The obj: ', my_dict, 'Deepcopy:', new_dict_copied_deep)


if __name__ == '__main__':
    main()
