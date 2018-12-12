import numpy as np
from collections import defaultdict

data = open("input.txt").read().split('\n')

coordinates = [[int(i.split(",")[0]), int(i.split(",")[1])] for i in data]
coordinates = list(enumerate(coordinates))
maxX = max([c[1][0] for c in coordinates])
minX = min([c[1][0] for c in coordinates])
maxY = max([c[1][1] for c in coordinates])
minY = min([c[1][1] for c in coordinates])
grid = np.zeros((maxY+1, maxX+1))
record = defaultdict(lambda: 0)
safePoints = 0

def dist(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])

def calcMinDist(p):
    d = dist(p, coordinates[0][1])
    n = 0
    equallyFar = 0
    for i in range(1, len(coordinates)):
        if dist(p, coordinates[i][1]) < d:
            equallyFar = 0
            d = dist(p, coordinates[i][1])
            n = coordinates[i][0]
            grid[p[1]][p[0]] = n
        elif dist(p, coordinates[i][1]) == d:
            equallyFar = 1
            grid[p[1]][p[0]] = -1
    else: 
        if equallyFar == 0: 
            record[n] += 1

def calcFinitePoints():
    finitePoints = []

    for c in coordinates:
        success = 0

        tempX = c[1][0]
        tempY = c[1][1]
        while tempX != minX:
            tempX -= 1
            if grid[tempY][tempX] == -1 or grid[tempY][tempX] != c[0]:
                success += 1
                break
        
        tempX = c[1][0]
        while tempX != maxX:
            tempX += 1
            if grid[tempY][tempX] == -1 or grid[tempY][tempX] != c[0]:
                success += 1
                break
        
        tempY = c[1][1]
        tempX = c[1][0]
        while tempY != minY:
            tempY -= 1
            if grid[tempY][tempX] == -1 or grid[tempY][tempX] != c[0]:
                success += 1
                break

        tempY = c[1][1]
        while tempY != maxY:
            tempY += 1
            if grid[tempY][tempX] == -1 or grid[tempY][tempX] != c[0]:
                success += 1
                break
        
        if success == 4: finitePoints.append(c)
    
    return finitePoints

def calcMaxArea(pts):
    area = []
    for p in pts:
        area.append(record.get(p[0]))
    
    return max(area)

def calcTotalDistance(p):
    global safePoints
    total = 0
    for c in coordinates:
        total += dist(p, c[1])
    
    if total < 10000: safePoints += 1

for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        calcMinDist([x, y])
        calcTotalDistance([x, y])
    
print(calcMaxArea(calcFinitePoints()))
print(safePoints)