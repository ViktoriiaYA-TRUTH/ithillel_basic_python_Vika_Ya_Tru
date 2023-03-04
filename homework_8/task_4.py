def gen_primes(i):  # returns list of ints
    result = True
    if i < 2:
        result = False
    else:
        for j in range(2, i):
            if i%j == 0:
                result = False
    return result


def main():
    for i in range(1, 101):
        if gen_primes(i):
            if i == 97:
                print(i)
            else:
                print(i)


if __name__ == '__main__':
    main()

