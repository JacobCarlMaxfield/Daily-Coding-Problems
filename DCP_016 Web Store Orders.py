"""
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. 
i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""

def record(order_id):
    with open('orders.txt', 'a') as f:
        f.write(str(order_id)+'\n')

def get_last(index):
    with open('orders.txt', 'r') as f:
        orders = f.readlines()
        print(orders)
        return int(orders[-index])

record(3425)
print(get_last(0))
