from phonebook import Phonebook

def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Bob", "12345")
    number = phonebook.lookup("Bob")
    assert number == "12345"
    
