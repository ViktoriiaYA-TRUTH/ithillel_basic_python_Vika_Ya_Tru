from random import randint


print('Guess number from 1 till 10')
number = randint(1, 10)
guess = int(input('Enter the number: '))
if guess == number:
    print('Hurray! The number is ', number)
    while guess != number:
        guess = int(input('Try again!'))
        if guess < number:
            print('The number is bigger')
        elif guess > number:
            print('The number is smaller')
