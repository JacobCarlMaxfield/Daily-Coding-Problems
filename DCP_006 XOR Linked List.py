"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, 
it holds a field named both, which is an XOR of the next node and the previous node. 
Implement an XOR linked list; it has an add(element) which adds the element to the end, 
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer functions 
that converts between nodes and memory addresses.
"""


class Node:
    def __init__(self, val, both=[None, None]):
        self.val = val
        self.both = both

    def add(self, element):
        current_node = self
        while current_node.both[1]:
            current_node = current_node.both[1]
        
        current_node.both[1] = Node(element, [current_node, None])
        return "Added %i to the linked list." % element


    def get(self, index):
        if index < 0:
            return "There is no node at index %i." % index
        n = 1
        current_node = self
        while current_node.both[1] and n <= index:
            current_node = current_node.both[1]
            n += 1
        if n <= index:
            return "There is no node at index %i." % index
        return current_node.val


node = Node(3)
print(node.add(17))
print(node.add(324))
print(node.add(43))

print(node.get(-1))
int()
