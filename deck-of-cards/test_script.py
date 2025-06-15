import unittest
import random
import collections
from typing import List
from my_decks import Solution


def make_deck(group_size: int, groups: int) -> List[int]:
    """
    Build a deck where every distinct card label appears
    exactly `group_size` times.  Used for stress testing.
    """
    deck = []
    base = 10_000_000
    for i in range(groups):
        deck.extend([base + i] * group_size)
    random.shuffle(deck)
    return deck


class TestSolution(unittest.TestCase):
    def test_edge_and_small_cases(self):
        cases = [
            ([], False),  # empty input
            ([5], False),  # single card
            ([2, 2], True),  # minimal positive (gcd = 2)
            ([1, 1, 2, 2, 3, 3], True),  # gcd = 2
            ([1, 1, 1, 2, 2, 2, 3, 3, 3], True),  # gcd = 3
        ]
        for deck, expected in cases:
            with self.subTest(deck=deck):
                self.assertEqual(Solution().hasGroupsSizeX(deck), expected)

    # negative
    def test_gcd_equal_one(self):
        bad_decks = [
            [1, 2],  # two singles
            [4, 4, 4, 6, 6, 8],  # counts (3, 2, 1)
            [9, 9, 5, 5, 5, 7, 7, 7, 7],  # counts (2, 3, 4)
        ]
        for deck in bad_decks:
            with self.subTest(deck=deck):
                self.assertFalse(Solution().hasGroupsSizeX(deck))

    # stress
    def test_large_shuffled_deck(self):
        for group_size in (2, 3, 4, 5, 7):
            with self.subTest(group_size=group_size):
                deck = make_deck(group_size=group_size, groups=10_000)
                self.assertTrue(Solution().hasGroupsSizeX(deck))

    # brute force + math.gcd

    # calculates the real gcd using math.gcd
    # and checks that the function returns True if and only if that GCD is 2 or more
    def test_counter_logic_matches_builtin_gcd(self):
        import math
        rng = random.Random(42)
        for _ in range(200):
            deck = [rng.randint(0, 5) for _ in range(rng.randint(0, 20))]
            vals = collections.Counter(deck).values()
            true_gcd = 0
            for v in vals:
                true_gcd = math.gcd(true_gcd, v)
            expected = true_gcd >= 2
            with self.subTest(deck=deck):
                self.assertEqual(Solution().hasGroupsSizeX(deck), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
