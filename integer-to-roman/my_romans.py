from typing import List, Dict

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert int to roman

        table = [
                ... more to add
                (10,   "X"), (9,    "IX"), (5,   "V"), (4,   "IV"),
                (1,    "I"),
                ]
        """
        val_map: List[tuple[int, str]] = [
            (10,   "X"), (9,   "IX"), (5,   "V"), (4,   "IV"),
            (1,    "I"),
        ]
        res = []
        #for val, sym in table:
        #    count, num = divmod(num, val)
        #    res.append(sym * count)
        #return "".join(res)

        raise NotImplementedError

    def romanToInt(self, s: str) -> int:
        """Convert roman numeral to int  (not ready)"""
        raise NotImplementedError