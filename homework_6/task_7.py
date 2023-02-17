def rec_fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)


print(rec_fibonacci(20))


