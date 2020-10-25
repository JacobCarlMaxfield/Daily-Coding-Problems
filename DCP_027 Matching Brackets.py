"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def matchingBrackets(bracket_string):
    bracketlist = []
    for bracket in bracket_string:
        if bracket in '({[':
            bracketlist.append(bracket)
        else:
            try:
                bracket_match = bracketlist.pop()
            except IndexError:
                return False
            if bracket_match == '{':
                if bracket != '}':
                    return False
            if bracket_match == '[':
                if bracket != ']':
                    return False
            if bracket_match == '(':
                if bracket != ')':
                    return False
    return True

print(matchingBrackets('((((((({{{}}})))){{}})))'))
print(matchingBrackets('{()}}{}{}))'))