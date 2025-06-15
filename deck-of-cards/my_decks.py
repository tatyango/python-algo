from typing import List
import collections

# find the greatest common divisor using iteration
#
#   | complexity                          | build count   | divisibility search | total       |
#   |-------------------------------------|---------------|---------------------|-------------|
#   | time (worst case)                   | O(n)          | O(n²)               | O(n²)       |
#   | space                               | O(m)          | —                   | O(m)        |
#

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2: return False
        vals = collections.Counter(deck).values()
        for n in range(2, max(vals) + 1):
            if all(v % n == 0 for v in vals): return True
        return False

# following is how actually people in internet solved
# time: amortized O(n)
# space remains O(m)


#   | complexity | frequency map (defaultdict + list)       | gcd reduction pass | total                    |
#   |------------|------------------------------------------|--------------------|--------------------------|
#   | Time       | O(n) & dict ops are average O(1)         | O(m · log k)       | O(n + m · log k) ≈ O(n)  |
#   | Space      | O(m) storing m counts & contentReference | —                  | O(m)                     |


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        mp = defaultdict(int)

        for card in deck:
            mp[card] += 1

        mpvalues = list(mp.values())
        g = mpvalues[0]
        for value in mpvalues:
            g = gcd(g, value)

        if g == 1:
            return False
        return True
