number = int(input('Введіть рік і я скажу чи він високосний: '))
if number == 0:
    print('Введіть більше 0')
elif number % 4 == 0 or number % 400 == 0 and number % 100 != 0:
    print('YES')
else:
    print('NO')

