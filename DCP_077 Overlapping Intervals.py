"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

def overlapping_intervals(intervals):
    intervals = [list(x) for x in intervals]
    interval_list = []
    for interval in intervals:
        for v in interval_list:
            if v[0] <= interval[0] <= v[1] or \
                v[0] <= interval[1] <= v[1] or \
                interval[0] <= v[1] <= interval[1] or \
                interval[0] <= v[1] <= interval[1]:
                
                v[0] = min(v[0], interval[0])
                v[1] = max(v[1], interval[1])
                break
        else:
            interval_list.append(interval)

    return interval_list

print(overlapping_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))

print(overlapping_intervals([(6, 12), (5, 20), (2, 5), (9, 90)]))