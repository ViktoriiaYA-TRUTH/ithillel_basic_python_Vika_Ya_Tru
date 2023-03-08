import random


def diff_odd_even(num_limit, lower_bound, upper_bound): # returns int
    number = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    evens = sum(n for n in number if n % 2 == 0)
    odds = sum(n for n in number if n % 2 != 0)
    return evens - odds


print(diff_odd_even(10, 0, 567))

