def gen_primes(*i):  # returns list of ints
    result = []
    for j in range(*i):
        if j == 0 or j == 1:
            continue
        else:
            for k in range(2, int(j/2) + 1):
                if j % k == 0:
                    break
            else:
                result.append(j)
    return result


print(gen_primes(1, 100))


