"""
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked 
only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. 
Otherwise, it should lock it and return true.

unlock, which unlocks the node. If it cannot be unlocked, then it should return false. 
Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. 
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
Each method should run in O(h), where h is the height of the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False

    def is_locked(self):
        return self.locked

    def lock(self):
        if self.is_locked():
            return False
        else:
            return_code = True
        parent_list = []
        if self.parent:
            parent_list.append(self.parent)

        x = 0
        while x < len(parent_list):
            if parent_list[x].parent:
                if parent_list[x].is_locked():
                    return_code = False
                    break
                parent_list.append(parent_list[x].parent)
            x += 1
        else:
            return_code = True
        
        child_nodes = []
        if self.left:
            child_nodes.append(self.left)
        if self.right:
            child_nodes.append(self.right)
        
        x = 0
        while x < len(child_nodes):
            if child_nodes[x].is_locked():
                return_code = False
                break
            if child_nodes[x].left:
                child_nodes.append(child_nodes[x].left)
            if child_nodes[x].right:
                child_nodes.append(child_nodes[x].right)
            x += 1
        else:
            return_code = True
            
        self.locked = return_code
        return return_code

    def unlock(self):
        if not self.is_locked():
            return False
        else:
            return_code = True
        
        parent_list = []
        if self.parent:
            parent_list.append(self.parent)
            
        x = 0
        while x < len(parent_list):
            if parent_list[x].parent:
                if parent_list[x].is_locked():
                    return_code = False
                    break
                parent_list.append(parent_list[x].parent)
            x += 1
        else:
            return_code = True
        
        child_nodes = []
        if self.left:
            child_nodes.append(self.left)
        if self.right:
            child_nodes.append(self.right)
        
        x = 0
        while x < len(child_nodes):
            if child_nodes[x].is_locked():
                return_code = False
                break
            if child_nodes[x].left:
                child_nodes.append(child_nodes[x].left)
            if child_nodes[x].right:
                child_nodes.append(child_nodes[x].right)
            x += 1
        else:
            return_code = True
        self.locked = not return_code
        return return_code
        


node = Node('root', Node('left', Node('left.left')), Node('right'))
node.parent = Node('parent', node)
print(node.lock())
print(node.unlock())