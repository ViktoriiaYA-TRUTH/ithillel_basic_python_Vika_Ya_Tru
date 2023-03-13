import random


def permtuate(text):
    words = text.split(' ')

    for word in words:
        first_char = word[0]
        last_char = word[-1]
        middle = word[1:-1]
        shuffled_middle_chars_list = []

        while len(middle) >= 3:
            every_three = middle[:3]
            middle = middle[3:]
            shuffled_3 = ''.join(random.sample(every_three, len(every_three)))

            if shuffled_3 != every_three:
                shuffled_middle_chars_list.append(shuffled_3)

        if middle:
            shuffled_middle_chars_list.append(middle)

    middle_good = ''.join(shuffled_middle_chars_list)
    shuffled_words = [first_char + middle_good + last_char for _ in words]
    return ' '.join(shuffled_words)


def main():
    text = input('Enter your text: ')
    print(permtuate(text))


if __name__ == '__main__':
    main()
