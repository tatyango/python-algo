import unittest
from my_romans import Solution

class TestRoman(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_roman_to_int_examples(self):
        cases = {
            "III": 3,
            "IV": 4,
            "MCMXCII": 1992,
            "LVIII": 58
        }
        for roman, value in cases.items():
            with self.subTest(roman=roman):
                self.assertEqual(self.s.romanToInt(roman), value)


    def test_int_to_roman_examples(self):
        cases = {
            3: "III",
            4: "IV",
            58: "LVIII",    # 50 + 5 + 3
            1992: "MCMXCII" # 1000 + 900 + 90 + 2
        }
        for value, roman in cases.items():
            with self.subTest(value=value):
                self.assertEqual(self.s.intToRoman(value), roman)

    def test_repeats(self):
        repeats = {
            3:"III",
            30: "XXX",
            300: "CCC",
        }
        for num, roman in repeats.items():
            with self.subTest(num=num):
                self.assertEqual(self.s.intToRoman(num), roman)
                self.assertEqual(self.s.romanToInt(roman), num)

    def test_mixed_complex_values(self):
        complex_values = {
            2421:"MMCDXXI",             # 2000 (MM) + 400 (CD) + 20 (XX) + 1 (I)
            3888: "MMMDCCCLXXXVIII"     # 3000 (MMM) + 800 (DCCC) + 80 (LXXX) + 8 (VIII)
        }
        for num, roman in complex_values.items():
            with self.subTest(num=num):
                self.assertEqual(self.s.intToRoman(num), roman)
                self.assertEqual(self.s.romanToInt(roman), num)

if __name__ == "__main__":
    unittest.main()
