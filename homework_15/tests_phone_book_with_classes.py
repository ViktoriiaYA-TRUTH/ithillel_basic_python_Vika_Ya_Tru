import unittest
from phone_book_with_classes import PhoneBook


class TestPhoneBook(unittest.TestCase):

    def test_add_entry_phonebook(self):
        phonebook = PhoneBook()
        entry = {'surname': 'Test', 'name': 'Test', 'age': 20, 'phone_number': '1234567890', 'address': 'Test'}
        phonebook.add_entry_phonebook(entry)
        self.assertEqual(phonebook.phone_book[-1], entry)

    def test_find_entry_name_phonebook(self):
        phonebook = PhoneBook(phone_book=[{'surname': 'Test', 'name': 'Test', 'age': 20, 'phone_number': '1234567890', 'address': 'Test'}])
        name = 'Test'
        expected_output = {'surname': 'Test', 'name': 'Test', 'age': 20, 'phone_number': '1234567890', 'address': 'Test'}
        self.assertEqual(phonebook.find_entry_name_phonebook(name), expected_output)

    def test_find_entry_age_phonebook(self):
        phonebook = PhoneBook(phone_book=[{'surname': 'Test1', 'name': 'Test1', 'age': 20, 'phone_number': '1234567890', 'address': 'Test1'},
                                          {'surname': 'Test2', 'name': 'Test2', 'age': 30, 'phone_number': '1234567890', 'address': 'Test2'}])
        age = 20
        expected_output = [{'surname': 'Test1', 'name': 'Test1', 'age': 20, 'phone_number': '1234567890', 'address': 'Test1'}]
        self.assertEqual(phonebook.find_entry_age_phonebook(age), expected_output)
