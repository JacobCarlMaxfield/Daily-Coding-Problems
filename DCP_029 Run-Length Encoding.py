"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""

decoded_string = "AAAABBBCCDAA"
encoded_string = "4A3B2C1D2A"

encoded = []

pos = 1
number = 1
character = decoded_string[0]

while True:
    if pos == len(decoded_string):
        encoded.append(f'{number}{character}')
        break
    if decoded_string[pos] == character:
        number += 1
    else:
        encoded.append(f'{number}{character}')
        character = decoded_string[pos]
        number = 1
    pos += 1

print(''.join(encoded))


decoded = []

character_pos = 1
number_pos = 0

while True:
    if number_pos == len(encoded_string):
        break
    decoded.append(encoded_string[character_pos] * int(encoded_string[number_pos]))
    character_pos += 2
    number_pos += 2

print(''.join(decoded))
