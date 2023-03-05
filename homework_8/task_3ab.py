lst = [167, 343, 6.7, 6.2, '9', '8', '5']
print(sorted(lst, key=float))


lst = [472, 326, 1, 999.0, '1101000', '99', 9, '20', 863, '0']
print(sorted(lst, key=lambda x: str(x)[0]))

