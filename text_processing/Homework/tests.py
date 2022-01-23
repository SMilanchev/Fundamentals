import unittest
from solution import find_length


class SolutionTest(unittest.TestCase):
    def test_for_length_is_true(self):
        self.assertEquals(find_length("too_long_username"), 17)
