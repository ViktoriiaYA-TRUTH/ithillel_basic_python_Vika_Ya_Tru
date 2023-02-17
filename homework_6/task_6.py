def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def main():
    x = int(input('Введіть число '))
    print(sign(x))


if __name__ == '__main__':
    main()