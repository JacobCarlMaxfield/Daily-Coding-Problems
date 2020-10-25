"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value 
are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) 
and constant space.
"""

def find_intersect(list_one_node, list_two_node):
    list_one = []
    list_two = []
    while True:
        if list_one_node:
            list_one.append(list_one_node.val)
        if list_two_node:
            list_two.append(list_two_node.val)
        if list_two_node.val in list_one:
            return list_two_node.val


