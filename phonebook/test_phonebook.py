import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add("Bob", "12345")

        number = phonebook.lookup("Bob")

        self.assertEqual(number, "12345")

    def test_missing_name(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.lookup("missing!")

    @unittest.skip("Work in progress")
    def test_empty_phonebook_is_consistent(self):
        phonebook = Phonebook()
        is_consistent = phonebook.is_consistent()
        self.assertTrue(is_consistent)