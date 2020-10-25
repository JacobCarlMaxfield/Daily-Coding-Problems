"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
"""

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def merge_sort_linked_lists(*roots):
    numbers = set()
    for root in roots:
        current = root
        while current:
            numbers.add(current.val)
            current = current.next
    numbers = sorted(numbers)
    current = Node(numbers[0])
    root = current
    for num in range(1, len(numbers)):
        current.next = Node(numbers[num])
        current = current.next

    current = root
    while current:
        print(current.val, end = ' ')
        current = current.next
    print()

    return root

print(merge_sort_linked_lists(Node(5, Node(9)), Node(1, Node(7))))
    