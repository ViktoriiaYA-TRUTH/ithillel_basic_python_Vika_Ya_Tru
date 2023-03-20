from random import randint


def get_integer(lower_bound=1, upper_bound=100, prompt=None):
    """
    Get input integer number from user
    :param lower_bound: entered number should be equal to or greater than lower bound
    :param upper_bound: entered number should be equal to or less than lower bound
    :param prompt: for used to get a number, which supplied
    :return: integer inputted from keyboard
    """

    if prompt is None:
        prompt = f'Enter an integer number between 1 and 100: '

    while True:
        try:
            input_text = input(prompt)
            number = int(input_text)
        except ValueError:
            print(f'{input_text} is not a integer number!')
            continue

        if number < lower_bound:
            print(f'Your number should be greater than or equal to {lower_bound}.')
            continue

        if number > upper_bound:
            print(f'Your number should be smaller than or equal to {upper_bound}.')
            continue

        break

    return number


def get_str(prompt, options):
    """
    Get text from user
    :return: entered text by user
    """
    while True:
        input_text = input(prompt).lower()
        if input_text not in options:
            print(f'Enter one of the given commands.')
        else:
            break
    return input_text


def guess_user():
    """
    Game mode: user's guess
    :return: if the number is less or greater than user's guess
    and congrats when won. Also calculates attempts
    """
    print('I will think of a number from 1 to 100, try to guess it')
    secret_num = randint(1, 100)
    attempts = 0
    while True:
        guess = get_integer(lower_bound=1, upper_bound=100, prompt='Enter the number:')
        attempts += 1
        if guess == secret_num:
            print(f'Congrats! You won for {attempts} attempts.')
            break
        elif guess < secret_num:
            print('The number is greater.')
        else:
            print('The number is smaller.')


def guess_program():
    """
    Game mode: program's guess
    :return: User guessed and number of attempts
    """
    print('Think of a number from 1 to 100, i\'ll try to guess it.')
    lower = 1
    upper = 100
    attempts = 0
    while True:
        guess = (lower + upper) // 2
        result = get_str(f'Is it right number {guess}? Enter "y" if right, enter '
                         f'"b" if your number is greater, "l" if smaller: ')
        attempts += 1
        if result == 'y':
            print(f'I guessed for {attempts} attempts.')
            break
        elif result == 'b':
            lower = guess + 1
        else:
            upper = guess - 1


def main():
    while True:
        choice = get_str('Which game mode would you choose? "u" '
                         '- you will guess the number, "c" - i will guess: ',
                         options=['c', 'u', 'b', 'l', 'y', 'yes', 'no'])

        if choice == 'u':
            guess_user()

        elif choice == 'c':
            guess_program()

        repeat = get_str('Would you like to continue? Enter "yes" if yes, "no" if no: ', options=['yes', 'no'])

        if repeat == 'no':
            break


if __name__ == '__main__':
    main()
