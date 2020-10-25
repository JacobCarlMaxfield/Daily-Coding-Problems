"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(root):
    prev = None
    current = root
    while current:
        current.next, prev, current = prev, current, current.next
    return prev


def r_print(current):
    temp = ''
    while current:
        print(current.val)
        temp += str(current.val) + ' '
        current = current.next
    return temp
node = Node(5, Node(2, Node(8, Node(22, Node(38)))))

r_list = reverse_linked_list(node)

print(r_print(r_list))