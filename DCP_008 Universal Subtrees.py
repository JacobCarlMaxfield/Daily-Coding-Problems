"""
This problem was asked by Google

 A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

 Given the root to a binary tree, count the number of unival subtrees.

 For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def universalSubtrees(root):
    current_node = None
    sp = 0
    stack = [root]
    while True:
        try:
            current_node = stack[sp]
        except:
            break
        if current_node.left:
            stack.append(current_node.left)
        if current_node.right:
            stack.append(current_node.right)
        sp += 1
    
    unival_trees = 0
    for node in stack:
        if node.left == node.right:
            unival_trees += 1
        elif node.left == None or node.right == None:
            pass
        elif node.left.val == node.right.val:
            unival_trees += 1
    
    return unival_trees


root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

print(universalSubtrees(root))

    