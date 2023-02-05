a = "mouse"
b = "cat"

c = a
a = b
b = c
print(a, b)

a = 'Uno'
b = 'Dos'

a, b = b, a
print(a, b)


a = 13
b = 48

a = a + b
b = a - b
a = a - b

print(a, b)
