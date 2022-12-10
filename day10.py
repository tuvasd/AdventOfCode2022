import sys

def lese(filename):
    with open(filename) as f:
        myList = [(list(line.strip().split())) for line in f]
        for item in myList:
            try:
               item[1] = int(item[1])
            except IndexError:
              gotdata = 'null'
    return myList
def findSignalStrength(commandList):
    result = [1]
    signalStrength = 1
    cycleNr = 1
    commandCounter = 0

    while commandCounter < len(commandList):
        command = commandList[commandCounter]

        if len(command) == 1:
            result.append(signalStrength)
            cycleNr += 1
            commandCounter += 1
        else:
            result.append(signalStrength)
            result.append(signalStrength)
            signalStrength += command[1]
            cycleNr += 2
            commandCounter += 1
    return result
def calcCrt(resultSignal):
    print(resultSignal)
    counter = 1
    for x in range(6):
        tmp = ""
        for y in range(40):
            posCur = resultSignal[counter]
            res = y - posCur
            if -1 <= res <= 1:
                tmp += "#"
            else:
                tmp += " "
            counter += 1
        print(tmp)
def findResult(resultSignal):
    intNr = [20,60,100,140,180,220]
    total = 0
    for nr in intNr:
        res = nr * resultSignal[nr]
        total += res
    return total

def part1(commandList):
    resultSignal = findSignalStrength(commandList)
    total = findResult(resultSignal)
    print(total)
    calcCrt(resultSignal)



file = sys.argv[1]
commandList = lese(file)
part1(commandList)