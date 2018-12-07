from collections import Counter

data = open("input.txt").read().split('\n')

# PART 1
two = 0 
three = 0
for box in data:
    d = Counter(box).values()
    if 2 in d: two += 1
    if 3 in d: three += 1

print(two * three)

# PART 2
def checkDiff(a, b):
    count = 0
    for i in range(0, len(a)):
        if a[i] != b[i]: count += 1
    return count

def removeDiff(a, b):
    i = 0
    while(i != len(a)-1):
        if a[i] != b[i]: a.pop(i)
        i += 1
    return a

def _():
    for i in range(0, len(data)):
        for j in range(i, len(data)):
            if checkDiff(data[i], data[j]) == 1:
                return "".join(removeDiff(list(data[i]), list(data[j])))

print(_())