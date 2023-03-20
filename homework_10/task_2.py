import string
import secrets


def gen_password(length):
    if length < 8:
        raise Exception('Too small password length')
    alphabet = string.ascii_letters + string.digits + '_'

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)):
            for i in range(length-1):
                if password[i] == password[i+1]:
                    break
            continue
        break

    return password


def main():
    print(gen_password(8))


if __name__ == '__main__':
    main()
