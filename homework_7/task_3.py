def main():
    kg = float(input('Введіть кількість кг: '))
    count_seeds_kg = kg / 0.000035
    seeds_on_position = 1
    for i in range(97, 105):
        for j in range(1, 9):
            seeds_on_position *= 2
            if seeds_on_position >= count_seeds_kg:
                print(f'Square: {chr(i) + str(j)}')
                break
        if seeds_on_position >= count_seeds_kg:
            break


if __name__ == '__main__':
    main()
