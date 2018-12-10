import json
import random
import unittest
from hard_952.solution_union_find import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largest_component_size_test_case_1(self):
        A = [4, 6, 15, 35]
        actual_output = self.solution.largestComponentSize(A)
        expected_output = 4
        self.assertEqual(expected_output, actual_output)

    def test_largest_component_size_test_case_2(self):
        A = [20, 50, 9, 63]
        actual_output = self.solution.largestComponentSize(A)
        expected_output = 2
        self.assertEqual(expected_output, actual_output)

    def test_largest_component_size_test_case_3(self):
        A = [2, 3, 6, 7, 4, 12, 21, 39]
        actual_output = self.solution.largestComponentSize(A)
        expected_output = 8
        self.assertEqual(expected_output, actual_output)

    def test_largest_component_size_test_case_4(self):
        A = [1, 73, 51, 84, 21, 55, 92, 93, 85]
        actual_output = self.solution.largestComponentSize(A)
        expected_output = 7
        self.assertEqual(expected_output, actual_output)

    def test_largest_component_size_test_case_5(self):
        with open('data_05.json') as f:
            A = json.load(f)
            import time
            start = time.time()
            self.solution.largestComponentSize(A)
            end = time.time()
            print(end - start)

    def test_largest_component_size_test_case_6(self):
        with open('data_06.json') as f:
            A = json.load(f)
            import time
            start = time.time()
            self.solution.largestComponentSize(A)
            end = time.time()
            print(end - start)