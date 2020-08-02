"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def abt(node):
    if node.val not in ['*', '/', '-', '+']:
        return node.val
    oper = node.val
    return eval("{} {} {}".format(abt(node.left), oper, abt(node.right)))



node = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
print(abt(node))