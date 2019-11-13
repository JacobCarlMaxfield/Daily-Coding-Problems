"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def decode(message, memo):
    if len(message) == 0:
        return 1
    if message[0] == '0':
        return 0
    if memo[message]:
        return memo[message]
    if len(message) == 1:
        return 1
    if int(message[0:2]) < 27:
        result = decode(message[1:], memo) + decode(message[2:], memo)
    else:
        result = decode(message[1:], memo)
    memo[message] = result
    return result

message = '111'
memo = dict()
for x in range(len(message)):
    memo[message[x:]] = None

print(decode(message, memo))
