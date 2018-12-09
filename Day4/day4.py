import re
from collections import OrderedDict, defaultdict, Counter

data = open("input.txt").read().split('\n')

# Data pre-processing
temp = dict()
for line in data:
    time = int("".join(re.findall("[0-9]+", line[:18])))
    desc = line[19:]
    temp[time] = desc
data = OrderedDict(sorted(temp.items()))

record = defaultdict(lambda: [0, []])
guard = None
falls = None
wakes = None
for time, desc in data.items():
    if "shift" in desc:
        guard = re.findall("[0-9]+", desc)[0]
    elif "falls" in desc:
        falls = time % 100
    elif "wakes" in desc:
        wakes = time % 100
        record[guard][0] += wakes - falls
        record[guard][1].extend([x for x in range(falls, wakes)])

# PART 1
def one():
    x = 0
    maxTimeGuard = 0
    mostCommonMinute = 0
    for i, [totalTime, minutes] in record.items():
        if x < totalTime: 
            maxTimeGuard = i
            x = totalTime
    mostCommonMinute = Counter(record[maxTimeGuard][1]).most_common()[0][0]

    return int(maxTimeGuard) * mostCommonMinute

print(one())

# PART 2
def two():
    x = 0
    mostCommonGuard = 0
    mostCommonMinute = 0
    for i, [totalTime, minutes] in record.items():
        if x < Counter(minutes).most_common()[0][1]:
            mostCommonGuard = i
            x = Counter(minutes).most_common()[0][1]
            mostCommonMinute = Counter(minutes).most_common()[0][0]
    
    return mostCommonMinute * int(mostCommonGuard)

print(two())