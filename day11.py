import sys
sys.set_int_max_str_digits(0)

class Monkey:
    def __init__(self, items, operation, test_nr, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.testNr = test_nr
        self.trueMonkey = true_monkey
        self.falseMonkey = false_monkey
        self.inspections = 0

    def doOperation(self,itemValue):
        if self.operation[2] == "old":
            if self.operation[1] == "*":
                return itemValue * itemValue
            else:
                return itemValue + itemValue
        else:
            if self.operation[1] == "*":
                return itemValue*int(self.operation[2])
            else:
                return itemValue + int(self.operation[2])

    def printMonkey(self):
        print("items: ", self.items)
        print("operation: ", self.operation)
        print("testNr: ", self.testNr)
        print("True monkey: ", self.trueMonkey)
        print("False Moneky: ", self.falseMonkey)


def lese(filename):
    myList = []
    with open(filename) as f:
        tmp = []
        for line in f:
            line = line.strip()
            if line == "":
                myList.append(makeMonkey(tmp))
                tmp = []
            else:
                tmp.append(line.split())
    myList.append(makeMonkey(tmp))
    return myList

def calcMulti(monkeyList):
    sum = 1
    for monkey in monkeyList:
        sum= sum * monkey.testNr
    return sum

def makeMonkey(liste):
    items = liste[1][2:]
    for i in range(len(items)):
        items[i] = int(items[i].replace(",","").strip())
    operation = liste[2][3:]
    testNr = int(liste[3][-1])
    trueMonkey = int(liste[4][-1])
    falseMonkey = int(liste[5][-1])
    monkey = Monkey(items, operation, testNr, trueMonkey, falseMonkey)
    return monkey

def round(monkeyList):
    multi = calcMulti(monkeyList)
    for x in range(10000):
        for monkey in monkeyList:
            monkeyRound(monkey, monkeyList,multi)

    nrInspections = []
    for monkey in monkeyList:
        nrInspections.append(monkey.inspections)
    nrInspections.sort()
    print(nrInspections)
    print(nrInspections[-1]*nrInspections[-2])

def monkeyRound(monkey,monkeyList,multi):
    while monkey.items:
        item = monkey.items.pop(0)
        newValue = monkey.doOperation(item)
        newValue = newValue % multi
        if newValue % monkey.testNr == 0:
            monkeyList[monkey.trueMonkey].items.append(newValue)
        else:
            monkeyList[monkey.falseMonkey].items.append(newValue)
        monkey.inspections += 1


file = sys.argv[1]
monkeyList = lese(file)
round(monkeyList)
