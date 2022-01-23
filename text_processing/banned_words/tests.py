import unittest
from solution import solution, get_digits, get_punctuation, get_alpha_characters


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        result = get_digits("Agd#53Dfg^&4F53")
        self.assertEquals(result, "53453")

    def test_solution_2(self):
        result = get_punctuation("Agd#53Dfg^&4F53")
        self.assertEquals(result, "#^&")

    def test_solution_3(self):
        result = get_alpha_characters("Agd#53Dfg^&4F53")
        self.assertEquals(result, "AgdDfgF")