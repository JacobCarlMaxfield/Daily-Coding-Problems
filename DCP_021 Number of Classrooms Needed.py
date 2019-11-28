"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures 
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
import random

def number_of_classrooms(class_times):
    current_classes = []
    overlapping_classes = 1
    
    for x, y in class_times:
        overlapping_classes_x = 1
        overlapping_classes_y = 1
        temp_classes = current_classes[:]
        for begin, end in temp_classes:
            if begin <= x < end:
                overlapping_classes_x += 1
            elif begin < y <= end:
                overlapping_classes_y += 1
        else:
            current_classes.append((x, y))
        overlapping_classes = max(overlapping_classes, 
                max(overlapping_classes_x, overlapping_classes_y))
    print(overlapping_classes, 'out of %i classes.' %  len(class_times))
    if len(class_times) == 0:
        return 0
    return overlapping_classes


number_of_classrooms(list((random.randint(1, 250), random.randint(150, 400)) 
                                for x in range(1) for y in range(200)))