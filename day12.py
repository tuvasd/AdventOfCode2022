import sys
from queue import PriorityQueue


def lese(filename):
    with open(filename) as f:
        myList = [(list(line.strip())) for line in f]
    return myList

def buildGraph(grid):
    dicGrid = {}
    lengthX = len(grid)
    lengthY = len(grid[0])
    tocheck = [(0,-1),(0,1),(-1,0),(1,0)]
    for x in range(0,lengthX):
        for y in range(0,lengthY):
            tmp = []
            currentLetter = grid[x][y]
            for deltaX,deltaY in tocheck:
                if x + deltaX == -1 or y+deltaY == -1:
                    continue
                try:
                    checkLetter = grid[x+deltaX][y+deltaY]
                    if checkLetters(currentLetter, checkLetter):
                        tmp.append((x + deltaX, y + deltaY))
                except IndexError:
                    continue
            dicGrid[(x,y)] = tmp
    return dicGrid

def checkLetters(current,neighboord):
    distanse = (ord(neighboord) - ord(current))
    if current == "S" and neighboord == "a":
        return True
    elif neighboord == "E":
        if current == "z":
            return True
        else:
            return False
    elif distanse <= 1:
        return True
    return False

def findletter(grid,letter):
    for i,line in enumerate(grid):
        if letter in line:
            return i,line.index(letter)


def dijkstra(dicGrid,start,end):
    visited = set()
    cost = {y: float('inf') for y in dicGrid}

    cost[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        (dist, current) = pq.get()
        if current == end:
            return dist
            break
        for neighbor in dicGrid[current]:
            if neighbor not in visited:
                old_cost = cost[neighbor]
                new_cost = cost[current] + 1
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    cost[neighbor] = new_cost

    return cost[end]
def findA(grid):
    aTuples = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "a":
                aTuples.append((i,j))
    return aTuples
def part1(grid):
    s_i, s_j = findletter(grid, "S")
    end_i, end_j = findletter(grid, "E")

    dicGrid = buildGraph(grid)

    cost = dijkstra(dicGrid, (s_i, s_j),(end_i,end_j))

    print("part 1: ", cost)


def part2(grid):
    dicGrid = buildGraph(grid)
    aTuples = findA(grid)

    #print(aTuples)

    maxCost = float('inf')
    end_i, end_j = findletter(grid, "E")

    for start in aTuples:
        #print(start)
        cost = dijkstra(dicGrid,start,(end_i,end_j))
        if cost < maxCost:
            maxCost = cost
            #print("new cost: ", maxCost)
    print("part 2: ", maxCost)



file = sys.argv[1]
grid = lese(file)
part1(grid)
part2(grid)
