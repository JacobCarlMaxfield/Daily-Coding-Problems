"""
This problem was asked by Google.

The edit distance between two strings refers to the minimum number of 
character insertions, deletions, and substitutions required to change 
one string to the other. 
For example, the edit distance between “kitten” and “sitting” is three: 
    substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def substitutions(string1, string2):
    # TODO find optimized position if multiple 'longest_substrings' are found.
    if not string1 or not string2:
        return max(len(string1), len(string2))

    s1 = string1
    s2 = string2
    longest_substring = ''
    for x in range(1, len(string1)):
        if string1[max(0, x-len(longest_substring)-1):x] in string2:
            longest_substring = string1[max(0, x-len(longest_substring)-1):x]
            ls = 's1'
    for x in range(1, len(string2)):
        if string2[max(0, x-len(longest_substring)-1):x] in string1:
            longest_substring = string2[max(0, x-len(longest_substring)-1):x]
            ls = 's2'

    s1_position = string1.index(longest_substring)
    s2_position = string2.index(longest_substring)

    s = ls

    s1 = ' ' * max(0, s2_position - s1_position) + s1
    s2 = ' ' * max(0, s1_position - s2_position) + s2
    s1 += ' ' * max(0, len(s2)-len(s1))
    s2 += ' ' * max(0, len(s1)-len(s2))
    
    print(s1)
    print(s2)

    total = 0
    for char in range(min(len(s1), len(s2))):
        if s1[char] != s2[char]:
            total += 1
    return total

print(substitutions('kitten', 'sitting'))