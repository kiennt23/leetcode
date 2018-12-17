import unittest

from medium_98.solution import Solution, TreeNode


def string_to_tree_node(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_valid_bst_test_case_1(self):
        input_str = "[1,1]"
        root = string_to_tree_node(input_str)
        actual_output = self.solution.isValidBST(root)
        self.assertFalse(actual_output)

    def test_is_valid_bst_test_case_2(self):
        input_str = "[10,5,15,null,null,6,20]"
        root = string_to_tree_node(input_str)
        actual_output = self.solution.isValidBST(root)
        self.assertFalse(actual_output)

    def test_is_valid_bst_test_case_3(self):
        input_str = "[5,14,null,1]"
        root = string_to_tree_node(input_str)
        actual_output = self.solution.isValidBST(root)
        self.assertFalse(actual_output)
