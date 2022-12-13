import sys
from queue import PriorityQueue

def compare(l,r):
    if isinstance(l,int) and isinstance(r,int):
        if r > l:
            return 1
        elif l > r:
            return -1
        else:
            return 0
    else:
        if isinstance(l,int):
            l = [l]
        if isinstance(r,int):
            r = [r]

        for le, re in zip(l, r):
            c = compare(le,re)
            if c != 0:
                return c
        if len(l) < len(r):
            return 1
        elif len(l) > len(r):
            return -1
        else:
            return 0

def lese(filename):
    myList = []
    with open(filename) as f:
        tmp = []
        for line in f:
            line = line.strip()
            if line == "":
                myList.append(tmp)
                tmp = []
            else:
                tmp.append(eval(line.strip()))
        #myList.append(tmp)
    return myList
def lese2(filename):
    myList = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            else:
                myList.append(eval(line.strip()))
    return myList
def part1(input):
    correct = [-1]
    for line in input:
        res = compare(line[0],line[1])
        #print(res)
        correct.append(res)

    sum = 0

    #print(correct)

    for i,ans in enumerate(correct):
        if ans == 1:
            sum += i

    print("part 1: ",sum)

def part2(filename):
    input = lese2(filename)
    packets = [input.pop(0)]
    for signal in input:
        counter = 0
        while compare(signal,packets[counter]) == -1:
            counter += 1
            if counter == len(packets):
                break
        packets.insert(counter,signal)

    index_2 = packets.index([[2]])+1
    index_6 = packets.index([[6]]) + 1

    print("part 2: " ,index_2*index_6)









file = sys.argv[1]
input = lese(file)
part1(input)
part2(file)