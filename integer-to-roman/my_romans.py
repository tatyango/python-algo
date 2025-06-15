from typing import List, Dict

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert int to roman
        """
        val_map: List[tuple[int, str]] = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10,   "X"),
            (9,   "IX"),
            (5,   "V"),
            (4,   "IV"),
            (1,    "I"),
        ]
        res = []
        for val, sym in val_map:
            count, num = divmod(num, val)
            res.append(sym * count)
        return "".join(res)

    def romanToInt(self, s: str) -> int:
        """Convert roman numeral to int  (not ready)"""
        raise NotImplementedError