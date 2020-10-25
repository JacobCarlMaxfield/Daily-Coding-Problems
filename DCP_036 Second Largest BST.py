"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Given the root to a binary search tree, find the second largest node in the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_nodes(value_list, skip_duplicates=True):
    if not skip_duplicates:
        if len(set(value_list)) < len(value_list):
            raise "Cannot have multiple of the same value"
    root = Node(value_list[0])
    for val in value_list[1:]:
        current = root
        while current:
            if val > current.val:
                if not current.right:
                    current.right = Node(val)
                    break
                current = current.right
            elif val < current.val:
                if not current.left:
                    current.left = Node(val)
                    break
                current = current.left
            
    return root

# Lazy!
def large_second(root):
    node_list = [root]
    node_values = []
    while node_list:
        node = node_list.pop(0)
        if node:
            node_values.append(node.val)
            node_list.extend([node.right, node.left])

    return sorted(node_values)[-2]


root = create_nodes([5, 9, 8, 7, 1, 4, 10, 3, 6, 2])
print(large_second(root))