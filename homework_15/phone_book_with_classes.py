import argparse
from class_utilities import Utilities


class PhoneBook:
    def __init__(self, phone_book=[]):
        """
        Initializes the PhoneBook class with a given phone_book.

        Args:
        - phone_book (list): A list of dictionary entries in the phonebook. Defaults to an empty list.

        Attributes:
        - phone_book (list): A list of dictionary entries in the phonebook.
        - changed_phone_book (bool): A boolean indicating whether the phonebook has been changed.
        """
        self.phone_book = phone_book
        self.changed_phone_book = False

    def print_phonebook(self):
        """
        Prints the entries in the phonebook.
        """
        print('\n\n #########  Phone book  ########## \n')

        number = 1
        for entry in self.phone_book:
            Utilities.print_entry(number, entry)
            number += 1

    def add_entry_phonebook(self):
        """
        Adds new entry
        """
        surname = input('    Enter surname: ')
        name = input('    Enter name: ')
        age = int(input('    Enter age: '))
        phone_number = input('    Enter phone num.: ')
        address = input('    Enter address: ')

        entry_new = {'surname': surname, 'name': name, 'age': age, 'phone_number': phone_number, 'address': address}
        self.phone_book.append(entry_new)
        self.changed_phone_book = True

    def find_entry_name_phonebook(self):
        """
        Finds entry by name from keyboard.
        """
        name = str(input('    Enter name: '))
        idx = 1
        found = False
        for entry in self.phone_book:
            if entry['name'] == name:
                Utilities.print_entry(idx, entry)
                idx += 1
                found = True
            if not found:
                Utilities.print_error('Not found!!')

    def find_entry_age_phonebook(self):
        """
        Finds entry by age from keyboard.
        """
        age = int(input('    Enter age: '))
        found_entries = []
        idx = 1
        for entry in self.phone_book:
            if entry['age'] == age:
                found_entries.append(entry)
                idx += 1
            if not found_entries:
                Utilities.print_error(' Not found!')
        else:
            for entry in found_entries:
                Utilities.print_entry(idx, entry)
                idx += 1

    def find_entry_address_phonebook(self):
        """
        Finds entry by address from keyboard
        """
        address = input(' Enter address: ').title()
        idx = 1
        found = False
        for entry in self.phone_book:
            if entry['address'] == address:
                Utilities.print_entry_address(idx, entry)
                idx += 1
                found = True
            if not found:
                Utilities.print_error(' Not found!')

    def delete_entry_name_phonebook(self):
        """
        Deletes entry by name from keyboard
        """
        name = input('    Enter name: ')
        phone_book_copy = self.phone_book.copy()
        for entry in phone_book_copy:
            if entry['name'] == name:
                self.phone_book.remove(entry)
        self.changed_phone_book = True

    def count_all_entries_in_phonebook(self):
        """
        Counts all entries
        """
        print('Total number of entries: ', len(self.phone_book))

    def print_phonebook_by_age(self):
        sorted_phone_book = sorted(self.phone_book, key=lambda entry: entry['age'])
        idx = 1
        for entry in sorted_phone_book:
            Utilities.print_entry_age(idx, entry)
            idx += 1

    def increase_age(self):
        """
        Increases age of all entries with a number from keyboard
        """
        new_age = int(input('    Enter number to increase age: '))
        for entry in self.phone_book:
            entry['age'] += new_age
        self.changed_phone_book = True

    def print_prompt(self):
        """
        Prints options what user can do
        """
        print('\n\n\n ~ Welcome to phonebook ~')
        print('Select one of actions below:')
        print('     1  - Print phonebook entries')
        print('     2  - Print phonebook entries (by age)')
        print('     3  - Add new entry')
        print('     4  - Find entry by name')
        print('     5  - Find entry by age')
        print('     55 - Find entry by address')
        print('     6  - Delete entry by name')
        print('     7  - The number of entries in the phonebook')
        print('     8  - Avr. age of all persons')
        print('     9  - Increase age by num. of years')
        print('------------------------------')
        print('     s  - Save to file')
        print('     l  - Load from file')
        print('     0  - Exit\n')

    def avr_age_of_all_persons(self):
        """
        Calculates average age of all.
        """
        total_age = 0
        num_persons = 0
        for contact in self.phone_book:
            total_age += contact['age']
            num_persons += 1
        if num_persons > 0:
            return total_age / num_persons
        else:
            return 0


class FileManager:
    """
    A class for working with files
    """
    def __init__(self, file_path):
        """
        Initialize a new instance of the FileManager class.
        """
        self.file_path = file_path
        self.phone_book = []
        self.changed_phone_book = False

    def exit(self):
        """
        Saves the phonebook to file if it has been changed before exiting the program.
        """
        if self.changed_phone_book is True:
            exit_save_or_not = input(' Do you want to save changes? Enter "yes" or "no": ')
            if exit_save_or_not.lower() == "yes":
                with open(self.file_path, "w") as file:
                    for entry in self.phone_book:
                        file.write(str(entry) + "\n")
                print('Phonebook saved successfully')

    def load_phonebook(self):
        """
        Loads the phonebook from the file specified by the file_path attribute.

        :return:
        list: A list of phonebook entries.
        """
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    entry = eval(line.strip())
                    self.phone_book.append(entry)
        except FileNotFoundError:
            pass

    def save_phonebook(self):
        """
        Saves the specified phonebook to the file specified by the file_path attribute.
        """
        with open(self.file_path, 'w') as file:
            for entry in self.phone_book:
                file.write(str(entry) + '\n')

def main():
    """
    This function runs the phonebook program. It allows the user to create, view,
    update, and delete entries in a phonebook, and to save the phonebook to a file
    and load it from a file.
    """
    parser = argparse.ArgumentParser(description='Phone book application')
    parser.add_argument('-f', '--filename', help='Load from file')
    args = parser.parse_args()

    phone_book = PhoneBook()

    if args.filename:
        phone_book = FileManager(args.filename).load_phonebook()

    while True:
        PhoneBook.print_prompt()

        choice = input('Enter your choice: ')
        if choice == '1':
            PhoneBook.print_phonebook()
        elif choice == '2':
            PhoneBook.print_phonebook_by_age()
        elif choice == '3':
            PhoneBook.add_entry_phonebook()
        elif choice == '4':
            PhoneBook.find_entry_name_phonebook()
        elif choice == '5':
            PhoneBook.find_entry_age_phonebook()
        elif choice == '55':
            PhoneBook.find_entry_address_phonebook()
        elif choice == '6':
            PhoneBook.delete_entry_name_phonebook()
        elif choice == '7':
            PhoneBook.count_all_entries_in_phonebook()
        elif choice == '8':
            print(f"The average age of all persons is {phone_book.avr_age_of_all_persons()}")
        elif choice == '9':
            PhoneBook.increase_age()
        elif choice == 's':
            FileManager.save_phonebook(phone_book.phone_book)
        elif choice == 'l':
            phone_book.phone_book = FileManager.load_phonebook()
        elif choice == '0':
            if phone_book.changed_phone_book:
                choice = input('Do you want to save changes? [y/n]: ')
                if choice == 'y':
                    FileManager.save_phonebook(phone_book.phone_book)
            break
        else:
             Utilities.print_error('Something went wrong. Try again...')


if __name__ == '__main__':
    main()
