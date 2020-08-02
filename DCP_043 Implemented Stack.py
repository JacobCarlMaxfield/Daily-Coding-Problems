"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.

"""

import sys

class Stack(list):
    def __init__(self, items=[]) -> None:
        self.items = items
        if not items:
            self.max_val = None
        else:
            self.max_val = max(items)

    def push(self, val):
        self.items.append(val)
        if self.max_val and self.max_val < val:
            self.max_val = val

    def pop(self):
        return self.items.pop()

    def max(self):
        return self.max_val

    def __repr__(self) -> str:
        return '[' + ', '.join([str(x) for x in self.items]) + ']'


l = Stack([1,2,3,4,5,6,7])

print(l.max())
l.push(50)
print(l)
l.pop()
print(l)