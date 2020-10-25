"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""
def combs(iterables):
    iters = iterables
    while len(iters) > 1:
        temp = []
        for x in iters[0]:
            for y in iters[1]:
                temp.append(x+y)
        iters = iters[2:]
        iters.insert(0, temp)
    return iters[0]

def num_let_rep(mapping, number):
    d = {str(x):y for x, y in mapping.items()}
    p = combs([d[n] for n in number])
    return p
    


print(num_let_rep({'2': ['a', 'b', 'c'], 3: ['d', 'e', 'f']}, '23'))
