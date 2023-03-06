import random

def diff_odd_even(num_limit, lower_bound, upper_bound): # returns int
    number = [random.randint(lower_bound, upper_bound) for _ in range(num_limit)]
    evens = 0
    odds = 0
    for i in range(0, num_limit):
        if i % 2 == 0:
            evens += number[i]
        elif i % 2 != 0:
            odds += number[i]
    return evens - odds


print(diff_odd_even(10, 0, 567))

