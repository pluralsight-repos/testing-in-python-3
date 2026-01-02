from phonebook import Phonebook

def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Bob", "12345")
    number = phonebook.lookup("Bob")
    assert number == "12345"
    
def test_contains_all_names():
    phonebook = Phonebook()
    phonebook.add("Bob", "12345")
    assert "Missing" in phonebook.all_names()
    assert phonebook.all_names() == {"Bob", "Missing"}