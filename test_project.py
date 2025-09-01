import unittest
from project import caesar_cipher

class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_simple(self):
        result = caesar_cipher("ABC", 1, "encrypt")
        self.assertEqual(result, "BCD")

    def test_encrypt_wraparound(self):
        result = caesar_cipher("XYZ", 3, "encrypt")
        self.assertEqual(result, "ABC")

    def test_decrypt_simple(self):
        result = caesar_cipher("BCD", 1, "decrypt")
        self.assertEqual(result, "ABC")

    def test_decrypt_wraparound(self):
        result = caesar_cipher("ABC", 3, "decrypt")
        self.assertEqual(result, "?.,")

    def test_encrypt_wraparound(self):
        result = caesar_cipher("abc", 5, "encrypt")
        self.assertEqual(result, "FGH")

    def test_perserve_nonletters(self):
        result = caesar_cipher("riley butler", 5, "encrypt")
        self.assertEqual(result, "WNQJ35GZYQJW")

    def test_case_insensitivity(self):
        result = caesar_cipher("hello", 2, "encrypt")
        self.assertEqual(result, "JGNNQ")

    def test_case_with_numbers(self):
        result = caesar_cipher("FYYFHP5FY56UR", 5, "decrypt")
        self.assertEqual(result,"ATTACK AT 1PM")

    def test_case_question(self):
        result = caesar_cipher("1MFYX5YMJ5FSX1JW5KTW5VZJXYNTS5?C", 5, "decrypt")
        self.assertEqual(result, "WHATS THE ANSWER FOR QUESTION 7?")


if __name__ == "__main__":
    unittest.main()


