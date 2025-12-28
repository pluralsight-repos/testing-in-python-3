import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Bob", "12345")