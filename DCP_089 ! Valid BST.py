"""
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint 
that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
"""


def valid_tree(root):
    # Only satisfies if the node's direct children are valid
    node_list = [root]
    while node_list:
        current = node_list.pop()
        if current.left:
            if current.left.val >= current.val:
                return False
            node_list.append(current.left)
        if current.right:
            if current.right.val <= current.val:
                return False
            node_list.append(current.right)
    return True
