"""
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

class Node():
    def __init__(self, val, next=None):
        self. val = val
        self.next = next

def kth_last_element(root, k):
    all_nodes = []
    current_values = [None for _ in range(k+1)]

    current_node = root
    while current_node:
        all_nodes.append(current_node)
        current_values.append(current_node)
        current_values = current_values[1:]
        current_node = current_node.next
    
    if None in current_values:
        for node in current_values:
            if node:
                node.next = None
                current_values.remove(node)
                return

    current_values[0].next = current_values[2]
    # all_nodes[-k-1].next = current_values[2]

    current_values[1].next = None
    # all_nodes[-k].next = None

    current_values.remove(current_values[1])
    # all_nodes.remove(all_nodes[-k])


    print([node.val for node in all_nodes], [node.val for node in current_values])
    return


kth_last_element(Node(0), 3)