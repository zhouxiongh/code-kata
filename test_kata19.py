import unittest

from kata19 import word_chain


class TestCase(unittest.TestCase):
    def test_basic(self):
        bank = ["cat", "cot", "cog", "dog"]
        start = bank[0]
        target = bank[-1]
        self.assertEqual(3, word_chain(start, target, bank))

        bank = ["lead", "load", "goad", "gold"]
        start = bank[0]
        target = bank[-1]
        self.assertEqual(3, word_chain(start, target, bank))

        bank = ["ruby", "rubs", "robs", "rods", "rode", "code"]
        start = bank[0]
        target = bank[-1]
        self.assertEqual(5, word_chain(start, target, bank))


if __name__ == "__main__":
    unittest.main()
