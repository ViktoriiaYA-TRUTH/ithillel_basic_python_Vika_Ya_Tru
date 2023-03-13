import string
import secrets


def gen_password(len):
    alphabet = string.ascii_letters + string.digits + '_'
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(len))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password)):
            break

    for c in password:
        if c * 3 in password:
            return False

    if len < 8:
        print('Your password must be at least 8 characters')
        return False

    return password


def main():
    print(gen_password(8))


if __name__ == '__main__':
    main()
