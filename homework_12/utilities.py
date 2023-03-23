def get_input_str(prompt, valid_options):
    while True:
        user_input = input(prompt).strip()
        if user_input in valid_options:
            return user_input
        else:
            print_error(f'Invalid input. '
                        f'Please enter one of the following '
                        f'options: {", ".join(valid_options)}')


def print_entry(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    print("| Phone:   %20s |" % entry["phone_number"])
    print("| Address:   %20s |" % entry["address"])
    print()


def print_entry_age(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    print("| Phone:   %20s |" % entry["phone_number"])
    print()


def print_entry_address(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name: %20s    |" % entry["name"])
    print("| Age: %20s     |" % entry["age"])
    print("| Phone: %20s   |" % entry["phone_number"])
    print("| Address: %20s |" % entry["address"])
    print()


def print_error(message):
    print("ERROR: %s" % message)


def print_info(message):
    print("INFO: %s" % message)


def print_status(func):
    def wrapper(*args, **kwargs):
        print('Starting to process your request')
        result = func(*args, **kwargs)
        print('Processing of your request completed')
        return result

    return wrapper

