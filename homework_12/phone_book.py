import os
running = True




#------------------------------------------------------------------------------
# Never use real phone/fax numbers for tests. Use 555 numbers:
# https://en.wikipedia.org/wiki/555_(telephone_number)
phone_book = [
{"name": "Nazar", "surname": "Nazarenko", "age": 50, "phone_number": "+18005550102", "address": "Kyiv"},
{"name": "Mariia", "surname": "Mariychuk", "age": 15, "phone_number": "+18505550112", "address": "Zhytomyr"},
]

changed_phone_book = False

#------------------------------------------------------------------------------
def print_entry(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    print("| Phone:   %20s |" % entry["phone_number"])
    print("| Address:   %20s |" % entry["address"])
    print()


#------------------------------------------------------------------------------
def print_entry_age(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ()


def print_entry_address(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name: %20s |" % entry["name"])
    print ("| Age: %20s |" % entry["age"])
    print ("| Phone: %20s |" % entry["phone_number"])
    print ("| Address: %20s |" % entry["address"])
    print ()



#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    global changed_phone_book
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number = input("    Enter phone num.: ")
    address = input("    Enter address: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["address"] = address
    phone_book.append(entry)
    changed_phone_book = True

#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input('    Enter age: '))
    found_entries = []
    idx = 1
    for entry in phone_book:
        if entry['age'] == age:
            found_entries.append(entry)
            idx += 1
    if not found_entries:
        printError(' Not found!')
    else:
        for entry in found_entries:
            print_entry(idx, entry)
            idx += 1


def find_entry_address_phonebook():
    address = input(" Enter address: ").title()
    idx = 1
    found = False
    for entry in phone_book:
        if entry["address"] == address:
            print_entry_address(idx, entry)
    idx += 1
    found = True
    if not found:
        printError(' Not found!')


#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    global changed_phone_book
    name = input('    Enter name: ')
    phone_book_copy = phone_book.copy()
    for entry in phone_book_copy:
        if entry['name'] == name:
            phone_book.remove(entry)
    changed_phone_book = True


#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    sorted_phone_book = sorted(phone_book, key=lambda entry: entry['age'])
    idx = 1
    for entry in sorted_phone_book:
        print_entry_age(idx, entry)
        idx += 1


#------------------------------------------------------------------------------
def increase_age():
    global changed_phone_book
    new_age = int(input('    Enter number to increase age: '))
    for entry in phone_book:
        entry['age'] += new_age
    changed_phone_book = True


    #------------------------------------------------------------------------------
def avr_age_of_all_persons():
    total_age = sum(entry['age'] for entry in phone_book)
    average_age = total_age / len(phone_book)

    printInfo(f'Average age of all persons: {average_age}')


#------------------------------------------------------------------------------
def save_to_file():
    global changed_phone_book
    if len(phone_book) == 0:
        printError('Phonebook is empty. Add new entry ')
        return
    save = input('Are you sure you want to save the phone book? Enter "yes" or "no": ')
    if save.lower() == "yes":
        file = open("phonebook.txt", "w")
        for entry in phone_book:
            file.write(str(entry) + "\n")
        file.close()
        printInfo('Phonebook saved successfully')
    changed_phone_book = True

#------------------------------------------------------------------------------
def load_from_file():
    global changed_phone_book
    if os.path.isfile('phonebook.txt'):
        if len(phone_book) > 0:
            save = input('Do you want to save changes? Enter "yes" or "no": ')
            if save.lower() == "yes":
                save_to_file()
            phone_book.clear()
        with open('phonebook.txt', 'r') as file:
            for line in file:
                entry = eval(line.strip())
                phone_book.append(entry)
        printInfo('Phonebook loaded successfully')
        changed_phone_book = True
    else:
        printError('No saved phone book found')


def my_function_change_age_by_name():
    global changed_phone_book
    name = input('    Enter name: ')
    phone_book_copy = phone_book.copy()
    for entry in phone_book_copy:
        if entry['name'] == name:
            new_age = int(input('    Enter new age: '))
            entry['age'] = new_age
    changed_phone_book = True


#------------------------------------------------------------------------------
def exit():
      global running, changed_phone_book
      running = False
      if changed_phone_book is True:
          exit_save_or_not = input(' Do you want to save changes? Enter "yes" or "no": ')
          if exit_save_or_not.lower() == "yes":
              file = open("phonebook.txt", "w")
              for entry in phone_book:
                  file.write(str(entry) + "\n")
              file.close()
              printInfo('Phonebook saved successfully')




#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1  - Print phonebook entries")
      print("     2  - Print phonebook entries (by age)")
      print("     3  - Add new entry")
      print("     4  - Find entry by name")
      print("     5  - Find entry by age")
      print("     55 - Find entry by address")
      print("     6  - Delete entry by name")
      print("     7  - The number of entries in the phonebook")
      print("     8  - Avr. age of all persons")
      print("     9  - Increase age by num. of years")
      print("------------------------------")
      print("     s  - Save to file")
      print("     l  - Load from file")
      print("     c  - Change age by name")
      print("     0  - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:
            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '55': find_entry_address_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,

                  '0':  exit,
                  'c':  my_function_change_age_by_name,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
