import json
from unittest import TestCase

from medium_142.solution import Solution, ListNode


# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def string_to_list_node(linked_list_str, pos=-1):
    # Generate list from the input
    numbers = json.loads(linked_list_str)

    # Now convert that list into linked list
    dummy_root = ListNode(0)
    ptr = dummy_root
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    last_ptr = ptr
    ptr = dummy_root.next
    pos_ptr = ptr
    if pos > -1:
        for i in range(pos):
            pos_ptr = pos_ptr.next
        last_ptr.next = pos_ptr
    return ptr


def list_node_to_string(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_detect_cycle_test_case_1(self):
        linked_list_str = "[3,2,0,-4]"
        pos = 1
        linked_list = string_to_list_node(linked_list_str, pos)
        cycle_start = self.solution.detectCycle(linked_list)
        self.assertEqual(2, cycle_start.val)

    def test_detect_cycle_test_case_2(self):
        linked_list_str = "[1,2]"
        pos = 0
        linked_list = string_to_list_node(linked_list_str, pos)
        cycle_start = self.solution.detectCycle(linked_list)
        self.assertEqual(1, cycle_start.val)

    def test_detect_cycle_test_case_3(self):
        linked_list_str = "[1]"
        pos = -1
        linked_list = string_to_list_node(linked_list_str, pos)
        cycle_start = self.solution.detectCycle(linked_list)
        self.assertIsNone(cycle_start)
