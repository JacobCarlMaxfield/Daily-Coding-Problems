"""
Daily Coding Problem #279
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

A classroom consists of N students, whose friendships can be represented in an adjacency list. 
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. 
In other words, this is the smallest set such that no student in the group has any friends outside this group. 
For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.

"""


def friend_groups(classroom):
    friend_group = []
    for x in classroom:
        v = {x}
        v.update(set(classroom[x]))
        friend_group.append(v)

    x = 0
    while x < len(friend_group):
        for o in range(len(friend_group)-1):
            for t in range(o+1, len(friend_group)):
                if any(num in friend_group[o] for num in friend_group[t]):
                    friend_group[o] = friend_group[o] | friend_group[t]
                    del friend_group[t]
                    break
        x += 1
    print(len(friend_group))


friend_groups({0: [1, 2],
               1: [0, 5],
               2: [0],
               3: [6],
               4: [],
               5: [1],
               6: [3]})
