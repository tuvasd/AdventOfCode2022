import copy
import sys
from copy import deepcopy


class Knot:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def moveR(self,deltax):
        self.x = self.x + deltax

    def moveU(self,deltay):
        self.y = self.y + deltay

    def moveL(self,deltax):
        self.x = self.x - deltax

    def moveD(self,deltay):
        self.y = self.y - deltay

    def getX(self):
        return self.x
    def getY(self):
        return self.y

def moveDiagonal(tail,deltaX, deltaY):
    if deltaX > 0:
        tail.x += 1
    elif deltaX < 0:
        tail.x -= 1
    if deltaY > 0:
        tail.y += 1
    elif deltaY < 0:
        tail.y -= 1

def doMove(letter,number, knot):
    if letter == "R":
        knot.moveR(number)
    elif letter == "U":
        knot.moveU(number)
    elif letter == "L":
        knot.moveL(number)
    else:
        knot.moveD(number)
def addToVisited(visited,endX,endY):
    if (endY,endX) not in visited:
        visited.append((endY,endX))
    return visited
def doCommand(letter,number,head,tail, visited):
    for i in range(number):
        doMove(letter,1,head)
        while not touching(head,tail):
            deltaY = head.y - tail.y
            deltaX = head.x - tail.x
            if deltaX == 0:
                if deltaY > 1:
                    doMove("U", 1, tail)
                else:
                    doMove("D", 1, tail)
            elif deltaY == 0:
                if deltaX > 1:
                    doMove("R", 1, tail)
                else:
                    doMove("L",1,tail)
            else:
                moveDiagonal(tail, deltaX,deltaY)
            print(tail.x, tail.y)
            addToVisited(visited, tail.x, tail.y)
    return visited

def doCommandNotVis(letter,number,head,tail):
    for i in range(number):
        while not touching(head,tail):
            deltaY = head.y - tail.y
            deltaX = head.x - tail.x
            if deltaX == 0:
                if deltaY > 1:
                    doMove("U", 1, tail)
                else:
                    doMove("D", 1, tail)
            elif deltaY == 0:
                if deltaX > 1:
                    doMove("R", 1, tail)
                else:
                    doMove("L",1,tail)
            else:
                moveDiagonal(tail, deltaX, deltaY)
def touching(head,tail):
    deltaY = head.y - tail.y
    deltaX = head.x - tail.x
    if 0 <= abs(deltaX) <= 1:
        if 0 <= abs(deltaY) <= 1:
            return True
    return False

def lese(filename):
    with open(filename) as f:
        myList = [(list(line.strip().split())) for line in f]
        for item in myList:
            item[1] = int(item[1])
    return myList
def printing(knots,visited,grid):
    currentCor = deepcopy(grid)

    counter = 0
    for knot in knots:
        currentCor[knot.y][knot.x] = str(counter)
        counter += 1
    currentCor[11][11] = "s"
    for line in currentCor[::-1]:
        print(line)

    print("-----------------")

    visited_grid = deepcopy(grid)

    for tup in visited:
        print("tup: ",tup)
        x = tup[0]
        y = tup[1]
        visited_grid[x][y] = "#"
    visited_grid[11][11] = "s"
    for line in visited_grid[::-1]:
        print(line)

def part1(moves):
    visited = []

    head = Knot(0,0)
    tail = Knot(0,0)

    addToVisited(visited,0,0)

    for move in moves:
        print(move)
        visited = doCommand(move[0],move[1],head,tail, visited)
    print(len(visited))


file = sys.argv[1]
moves = lese(file)
part1(moves)
