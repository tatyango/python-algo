import unittest
from my_romans import Solution

class TestRoman(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_roman_to_int_examples(self):
        cases = {
            "III": 3,
            "IV": 4,
        }
        for roman, value in cases.items():
            with self.subTest(roman=roman):
                self.assertEqual(self.s.romanToInt(roman), value)

    def test_int_to_roman_examples(self):
        cases = {
            3: "III",
            4: "IV",
        }
        for value, roman in cases.items():
            with self.subTest(value=value):
                self.assertEqual(self.s.intToRoman(value), roman)

if __name__ == "__main__":
    unittest.main()
