"""
This problem was asked by Palantir.

Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible,
with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
spaces = 16

total_length = sum([len(word) for word in words])
print(total_length)

lines = []

current_line = ''

x = 0
while x < len(words):
    if len(current_line) + len(words[x]) <= spaces:
        current_line += ' ' + words[x]
        x += 1
    else:
        lines.append(current_line[1:])
        current_line = ''
else:
    lines.append(current_line[1:])

for line in range(len(lines)):
    lines[line] = lines[line].split(' ')


justified = []

import math
for word_line in lines:
    working_line = ''
    spaces_left = spaces - sum([len(word) for word in word_line])
    words_left = len(word_line) - 1
    for word in word_line:
        working_line += word
        if words_left > 0:
            appending_spaces = ' ' * math.ceil(spaces_left / words_left)
        else:
            appending_spaces = ''
        spaces_left -= len(appending_spaces)
        working_line += appending_spaces
        words_left -= 1
    justified.append(working_line)


print(justified)
