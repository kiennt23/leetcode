from functools import reduce


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.size = 1


def find(node):
    """Path compression"""
    if node.parent.value != node.value:
        node.parent = find(node.parent)
    return node.parent


def union(node1, node2):
    """Union by size"""
    root1 = find(node1)
    root2 = find(node2)
    if root1.value == root2.value:
        return root1

    if root1.size < root2.size:
        root1, root2 = root2, root1

    root2.parent = root1
    root1.size = root1.size + root2.size
    return root1


class Solution:
    def largestComponentSize(self, A):
        max_value = int(max(A))
        nodes = []
        for a in A:
            node = Node(a)
            nodes.append(node)
        largest_root = None
        prime_numbers = []
        from math import sqrt
        for i in range(2, max_value):
            prime = True
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                prime_numbers.append(i)
        for i in prime_numbers:
            nodes_to_merge = []
            tmp_root = None
            for node in nodes:
                if node.value % i == 0:
                    nodes_to_merge.append(node)
            if len(nodes_to_merge) > 1:
                tmp_root = reduce(union, nodes_to_merge)
            if tmp_root is not None:
                largest_root = tmp_root if largest_root is None or largest_root.size < tmp_root.size else largest_root
        return largest_root.size if largest_root is not None else 1
