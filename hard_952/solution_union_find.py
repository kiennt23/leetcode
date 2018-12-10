class Node:
    def __init__(self, index):
        self.value = index
        self.parent = self
        self.size = 1

    def __str__(self):
        return '[' + str(self.value) + ',' + str(self.parent.value) + ',' + str(self.size) + ']'


def find(node: Node):
    if node.parent.value != node.value:
        node.parent = find(node.parent)
    return node.parent


def union(node1: Node, node2: Node):
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
        max_value = max(A)
        nodes = []
        for a in A:
            node = Node(a)
            nodes.append(node)
        largest_root: Node = None
        for i in range(2, int(max_value)):
            nodes_to_merge = []
            tmp_root: Node = None
            for node in nodes:
                if node.value % i == 0:
                    nodes_to_merge.append(node)
            if len(nodes_to_merge) > 1:
                tmp_root = nodes_to_merge[0]
                for j in range(1, len(nodes_to_merge)):
                    tmp_root = union(tmp_root, nodes_to_merge[j])
            if tmp_root is not None:
                largest_root = tmp_root if largest_root is None or largest_root.size < tmp_root.size else largest_root
        return largest_root.size if largest_root is not None else 1
