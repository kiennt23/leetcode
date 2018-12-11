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

        def prime_factors(n):  # Prime factor decomposition
            out = set()
            while n % 2 == 0:
                out.add(2)
                n //= 2
            from math import sqrt
            for i in range(3, int(sqrt(n))+1, 2):
                while n % i == 0:
                    out.add(i)
                    n //= i
            if n > 2:
                out.add(n)
            return out

        nodes = []
        for a in A:
            node = Node(a)
            nodes.append(node)
        largest_root = None
        prime_to_nodes = {}
        for node in nodes:
            primes = prime_factors(node.value)
            for prime in primes:
                tmp_root = node
                if prime in prime_to_nodes:
                    tmp_root = union(node, prime_to_nodes[prime])
                if tmp_root is not None:
                    prime_to_nodes[prime] = tmp_root
        for key, value in prime_to_nodes.items():
            largest_root = value if largest_root is None or largest_root.size < value.size else largest_root
        return largest_root.size if largest_root is not None else 0
