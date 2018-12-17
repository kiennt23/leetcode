# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        return self.validate_bst(root, - sys.maxsize - 1, sys.maxsize)

    def validate_bst(self, node, n_min, n_max):
        if not node:
            return True
        if n_min >= node.val or node.val >= n_max:
            return False
        return self.validate_bst(node.left, n_min, node.val) and self.validate_bst(node.right, node.val, n_max)
