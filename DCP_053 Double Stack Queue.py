"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a queue using two stacks. 
Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: 
enqueue, which inserts an element into the queue, 
and dequeue, which removes it.
"""

class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, value):
        self.s1.append(value)

    def dequeue(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        if self.s2:
            value = self.s2.pop()
        else:
            value = None
        while self.s2:
            self.s1.append(self.s2.pop())
        return value
        