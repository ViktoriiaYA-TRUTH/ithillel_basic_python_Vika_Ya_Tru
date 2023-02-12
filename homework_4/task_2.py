a = input('Enter name, date of birth and date of death (in format name*year-month-day*year-month-day): ')
c = a[a.find('*'):]
d = int(c[-10:-6]) - int(c[1:5])


print('\U000025CF ','Name:', a[:a.find('*')], '\n'
      '\U000025CF ', 'Age: ', d, 'years')

