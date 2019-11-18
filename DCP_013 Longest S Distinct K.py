"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring 
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, 
the longest substring with k distinct characters is "bcb".
"""

def distinctKSubstring(string, k):
    longest_substring = ''
    for start_char in range(len(string)):
        current_substring = ''
        character_count = 0
        for char in string[start_char:]:
            if char not in current_substring:
                if character_count == k:
                    if len(current_substring) > len(longest_substring):
                        longest_substring = current_substring[:]
                        break
                character_count += 1
            current_substring += char
    if len(longest_substring) == 0:
        if k > 0:
            return string
    return longest_substring


print(distinctKSubstring(''.join(['abc' for _ in range(10)]), 3))  
