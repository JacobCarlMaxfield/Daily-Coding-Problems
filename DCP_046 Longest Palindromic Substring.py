"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""

def lps(string):
    longest = ''
    for x in range(len(string)):
        for y in range(x+1, len(string)+1):
            if string[x:y] == string[y-1:x-1:-1]:
                if len(string[x:y]) > len(longest):
                    longest = string[x:y]
    return longest

print(lps("aabcdcb"))
print(lps("bananas"))