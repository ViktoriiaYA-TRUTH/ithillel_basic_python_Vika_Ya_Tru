number = input("Введіть трьохзначне число: ")

a = int(number[0])
b = int(number[1])
c = int(number[2])

print("В сумі цифри утворюють:", a + b + c )




number = input("Введіть трьохзначне число: ")
number = int(number)

a = number % 10
b = number % 100 // 10
c = number // 100

print("В сумі цифри утворюють:", a + b + c )

