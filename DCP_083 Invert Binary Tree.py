"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""

def invert_tree(root):
    node_list = [root]
    while node_list:
        node = node_list.pop()
        left = node.left
        right = node.right
        node.left, node.right = node.right, node.left

        if node.left:
            node_list.append(node.left)
        if node.right:
            node_list.append(node.right)
    return root

    