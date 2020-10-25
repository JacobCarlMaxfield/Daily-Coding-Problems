"""
This problem was asked by Google.

Given the root to a binary tree,
implement serialize(root), which serializes the tree into a string,
and deserialize(s), which de-serializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""

import re
from collections import defaultdict

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    string = ''
    if root.val != 'root':
        string += '-root.' + root.val
    else:
        string += root.val

    if root.left:
        string += serialize(root.left)
    if root.right:
        string += serialize(root.right)

    return string


def deserialize(s):
    root_node = Node('root')
    string_list = s.split('-')
    for string in string_list:
        string = string.split('.')
        current_node = root_node
        for val in string:
            if val == 'left':
                if not current_node.left:
                    current_node.left = Node('.'.join(string[1:]))
                current_node = current_node.left
            elif val == 'right':
                if not current_node.right:
                    current_node.right = Node('.'.join(string[1:]))
                current_node = current_node.right

    return root_node


node = Node('root', Node('left', Node('left.left')), Node('right'))

print(serialize(node))
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(node)))
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(deserialize(serialize(node))))
assert deserialize(serialize(node)).left.left.val == 'left.left'
