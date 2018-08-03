import unittest
import caps

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = "python"
        result = caps.cap_text(text)
        self.assertEqual(result,"Python")

    def test_multi_word(self):
        text = "monty python"
        result = caps.cap_text(text)
        self.assertEqual(result,"Monty Python")

if __name__ == '__main__':
    unittest.main()