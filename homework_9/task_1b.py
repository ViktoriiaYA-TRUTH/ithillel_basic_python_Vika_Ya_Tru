import random

def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    result = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    max_result = result[0]
    min_result = result[0]
    for i in range(1, num_limit):
        if result[i] > max_result:
            max_result = result[i]
        elif result[i] < min_result:
            min_result = result[i]
    return max_result - min_result


def main():
    print(diff_min_max(10, 0, 567))


if __name__ == '__main__':
    main()
