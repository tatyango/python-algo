from typing import List
import collections

# find the greatest common divisor using iteration
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2: return False
        vals = collections.Counter(deck).values()
        for n in range(2, max(vals) + 1):
            if all(v % n == 0 for v in vals): return True
        return False
