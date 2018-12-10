import re
import string

data = open("input.txt").read()

# PART 1
def react(polymer):
    i = 0
    while i != len(polymer)-1:
        if abs(ord(polymer[i]) - ord(polymer[i+1])) == 32:
            polymer.pop(i)
            polymer.pop(i)
            if i != 0: i -= 1 
        else: i += 1
    
    return len(polymer)

print(react(list(data)))

# PART 2
def removeChar(c, polymer):
    i = 0
    while i != len(polymer):
        if polymer[i].lower() == c:
            polymer.pop(i)
        else:
            i += 1
    
    return polymer

def shortestPolymer():
    l = react(removeChar('a', list(data)))
    for c in string.ascii_lowercase[1:]:
        x = react(removeChar(c, list(data)))
        if x < l: l = x

    return l

print(shortestPolymer())