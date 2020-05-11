import unittest

from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        """
        The setUp method is called each time a test case is executed.
        :return: PhoneBook Class.
        """
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        """
        This class is used to release the resource which are used by the testcases like in the case of using some files for testing or maybe the use of some database or so. As of now in this code its not required and hence it is passed.
        """
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Arjun","12345")
        number = self.phonebook.lookup("Arjun")
        self.assertEqual("12345",number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("Missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("bob","123454")
        self.phonebook.add("Anna", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add("bob","123454")
        self.phonebook.add("Anna", "123454")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add("bob","12345")
        self.phonebook.add("Sue","123")
        self.assertFalse(self.phonebook.is_consistent())


