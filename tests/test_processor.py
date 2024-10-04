import unittest
from src.processor import count_words, count_chars, find_word, replace_word

class TestProcessor(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("Hello world"), 2)
        self.assertEqual(count_words(""), 0)

    def test_count_chars(self):
        self.assertEqual(count_chars("Hello world"), 11)
        self.assertEqual(count_chars(""), 0)

    def test_find_word(self):
        self.assertEqual(find_word("Hello world world", "world"), 2)
        self.assertEqual(find_word("Hello World", "world"), 1)  # Case-insensitive

    def test_replace_word(self):
        self.assertEqual(replace_word("Hello world", "world", "Python"), "Hello Python")
        self.assertEqual(replace_word("Hello World", "world", "Python"), "Hello Python")  # Case-insensitive

if __name__ == '__main__':
    unittest.main()