import pytest
from phonebook import Phonebook

@pytest.fixture
def phonebook():
    phonebook = Phonebook()
    return phonebook

def test_lookup_by_name(phonebook):
    # phonebook = Phonebook()
    phonebook.add("Bob", "12345")
    number = phonebook.lookup("Bob")
    assert number == "12345"
    
def test_contains_all_names(phonebook):
    # phonebook = Phonebook()
    phonebook.add("Bob", "12345")
    assert "Bob" in phonebook.all_names()
    assert phonebook.all_names() == {"Bob"}
    
def test_missing_name(phonebook):
    # phonebook = Phonebook()
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
    