def main():
    position_one = input('Введіть першочергову точку коня (літера і цифра): ')
    move_to = input('Введіть клітинку куди здійснюється хід (літера і цифра): ')
    letter1 = int(ord(position_one[:1]))
    number1 = int(position_one[1:])
    letter2 = int(ord(move_to[:1]))
    number2 = int(move_to[1:])
    if letter1 < 94 or letter1 > 104 or letter2 < 94 or letter2 > 104 or number1 < 1 or number1 > 8 or number2 < 1 or number2 > 8:
        print('Оберіть лише можливу клітинку шахівниці (літери a-h, числа від 1 до 8)')
    elif letter1 - letter2 == 0 and number1 - number2 == 0:
        print('Оберіть іншу клітинку, кінь не хоче стояти на місці!')
    elif (letter1 - letter2 == 1) or (letter1 - letter2 == -1) and (number1 - number2 == 2 or number1 - number2 == -2):
        print('YES')
    elif (letter1 - letter2 == 2) or (letter1 - letter2 == -2) and (number1 - number2 == 1 or number1 - number2 == -1):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
