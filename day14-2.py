import sys
from copy import deepcopy
def lese(filename):
    myList = []
    with open(filename) as f:
        for line in f:
            line = line.strip().split("->")
            tmp = []
            for i, element in enumerate(line):
                tmp = element.split(",")
                line[i] = (int(tmp[0].strip()),int(tmp[1].strip()))
            myList.append(line)
    return myList

def findXY(input):
    minx = float('inf')
    minY = float('inf')
    maxX = 0
    maxY = 0
    for element in input:
        for x,y in element:
            if x > maxX:
                maxX = x
            if x < minx:
                minx = x
            if y < minY:
                minY = y
            if y > maxY:
                maxY = y
    print([maxX - minx, maxY-minY])
    return [minx, minY, maxX, maxY]

def makeCave(input, minAndMax):
    minX = minAndMax[0] - 470
    minY = minAndMax[1]
    print(minAndMax[3])
    grid = []
    for _ in range(0,minAndMax[3]+2):
        tmp = []
        for _ in range(0,1000):
            tmp.append(".")
        grid.append(tmp)

    for line in input:
        for i in range(0,len(line)-1):
            first = line[i]
            second = line[i+1]

            x1_offset = first[0]
            x2_offset = second[0]
            if first[0] != second[0]:
                for x in range(min(x1_offset,x2_offset),max(x1_offset,x2_offset)+1):
                    grid[first[1]][x] = "#"
            elif first[1] != second[1]:
                for y in range(min(first[1],second[1]),max(first[1],second[1])+1):
                    grid[y][x1_offset] = "#"
    return grid
def movingOne(currentX, currentY,grid):
    moving = [(0,1),(-1,1),(1,1)]

    nextLine = grid[currentY+1]

    for item in moving:
        if nextLine[currentX + item[0]] == ".":
            currentX = currentX+item[0]
            currentY = currentY + 1
            if currentY+1 == len(grid):
                break
            return movingOne(currentX,currentY,grid)
    grid[currentY][currentX] = "*"
    if currentY == 0:
        return False

    return grid

def sand(grid, minX):
    startX = 500
    counter = 0

    while grid:
        grid = movingOne(startX, 0, grid)
        counter += 1
    print(counter)


file = sys.argv[1]
input = lese(file)
grid = makeCave(input,findXY(input))


sand(grid,findXY(input)[0])

