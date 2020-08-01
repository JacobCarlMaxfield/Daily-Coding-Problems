"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""

# O(2N) at most I think
def rgb_swap(rgb_list):
    front = 0
    back = len(rgb_list)-1
    x = 1
    count = 0
    while x <= back:
        count += 1
        if rgb_list[x] == 'R':
            rgb_list[x], rgb_list[front] = rgb_list[front], rgb_list[x]
            front += 1
        elif rgb_list[x] == 'B':
            rgb_list[x], rgb_list[back] = rgb_list[back], rgb_list[x]
            back -= 1
        else:
            x += 1
    print(count)
    return rgb_list

print(rgb_swap(['B'] * 50 + ['G'] * 50 + ['R'] * 50))
