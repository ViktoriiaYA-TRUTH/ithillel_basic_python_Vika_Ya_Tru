import random

def diff_min_max(num_limit, lower_bound, upper_bound): # returns int
    result = [random.randint(lower_bound, upper_bound) for i in range(num_limit)]
    return max(result) - min(result)


print(diff_min_max(10, 0, 567))
