def copydeep(obj, depth=1, memory=None):
    if memory is None:
        memory = {}

    if id(obj) not in memory:
        memory[id(obj)] = obj

    if depth == 1:
        return obj

    if isinstance(obj, list):
        result = []
        for elem in obj:
            result.append(copydeep(elem, depth=depth + 1, memory=memory))
        return result

    elif isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            result[copydeep(key, depth=depth + 1, memory=memory)] = copydeep(value, depth=depth + 1, memory=memory)
        return result

    elif isinstance(obj, tuple):
        result = list()
        for i in obj:
            result.append(copydeep(i))
        return tuple(result)

    elif isinstance(obj, (str, int, float, bool)):
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
