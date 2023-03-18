def copydeep(obj, memory=None):
    if memory is None:
        memory = {}

    obj_id = id(obj)
    if obj_id in memory:
        return memory[obj_id]
    else:

        if isinstance(obj, list):
            new_list = []
            memory[obj_id] = new_list
            for i in obj:
                new_list.append(copydeep(i, memory))
            return new_list

        if isinstance(obj, dict):
            new_dict = {}
            memory[obj_id] = new_dict
            for key, value in obj.items():
                new_dict[copydeep(key, memory)] = copydeep(value, memory)
            return new_dict

        if isinstance(obj, (str, int, float, bool)):
            result = obj
            return result


def main():
    test_data = [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658]}, 2.0, {'e': 0}]
    test_data[3]['d'] = test_data
    test_data[-1]['f'] = test_data[-1]
    copy = copydeep(test_data)
    print(test_data)
    # [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
    print(copy)
    # [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658], 'd': [...]}, 2.0, {'e': 0, 'f': {...}}]
    print(copy[3]['c'] is not test_data[3]['c'])  # True
    print(copy[3]['d'] is not test_data[3]['d'])  # True
    print(copy[3]['d'] is copy)  # True
    print(copy[-1] is not test_data[-1])  # True
    print(copy[-1] is copy[-1]['f'])  # True


if __name__ == '__main__':
    main()
