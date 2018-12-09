import random
import unittest
from hard_952.solution import Solution, InvalidElementException, InvalidArraySizeException


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

    def test_invalid_element_raise_exception(self):
        A = [2, 3, 6, 7, 100_001, 12, 21]
        with self.assertRaises(InvalidElementException) as context:
            self.solution.largestComponentSize(A)
        self.assertTrue("Element greater than 100000" in str(context.exception))

    def test_invalid_array_size_raise_exception(self):
        A = [random.random() for _ in range(20_001)]
        with self.assertRaises(InvalidArraySizeException) as context:
            self.solution.largestComponentSize(A)
        self.assertTrue("Array size greater than 20000" in str(context.exception))
