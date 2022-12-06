import sys
import re

def buildStack(liste):
    tmp = []
    full_stack = []
    rev = liste[::-1]
    for i in range(0,len(rev[0])):
        for j in range(1,len(rev)):
            try:
                string = rev[j][i].strip()
                if string != "":
                    tmp.append(string)
            except IndexError:
                break
        full_stack.append(tmp)
        tmp = []
    return full_stack

def lese(filename):
    with open(filename) as f:
        myList = []
        moves = []
        for line in f:
            line = line.strip("\n")
            print(line)
            if line == "":
                break
            n = 4
            myList.append([line[i:i + n] for i in range(0, len(line), n)])
        for line in f:
            res = (re.findall(r'\d+', line))
            moves.append(res)
    return myList, moves

def doMoves(stack, moves):
    for move in moves:
        number_of_moves = int(move[0])
        from_list = int(move[1]) - 1
        to_list = int(move[2]) - 1

        for x in range(number_of_moves):
            stack[to_list].append(stack[from_list].pop())
    return stack

def doMovesInOrder(stack, moves):
    for move in moves:
        number_of_moves = int(move[0])
        from_list = int(move[1]) - 1
        to_list = int(move[2]) - 1
        tmp = []
        for x in range(number_of_moves):
            tmp.append(stack[from_list].pop())
        for box in reversed(tmp):
            stack[to_list].append(box)
    return stack

def part1(stack):
    string = ""
    for row in stack:
        string += re.sub('[^a-zA-Z]+', '', row.pop())
    print(string)

file = sys.argv[1]
liste, moves = lese(file)
stack = buildStack(liste)
new_stack = doMovesInOrder(stack, moves)
part1(new_stack)



