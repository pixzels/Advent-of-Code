import re
import numpy as np

data = open("input.txt").read().split('\n')
fabric = np.zeros((1000, 1000))

# PART 1
for line in data:
    i, x, y, width, height = re.findall("[0-9]+", line)
    fabric[int(x):int(x)+int(width), int(y):int(y)+int(height)] += 1
print(np.sum(fabric > 1))

# PART 2
for line in data:
    i, x, y, width, height = re.findall("[0-9]+", line)
    if np.all(fabric[int(x):int(x)+int(width), int(y):int(y)+int(height)] == 1):
        print(i)
        break