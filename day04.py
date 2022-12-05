import sys
import copy


def lese(filename):
    with open(filename) as f:
        myList = []
        tmp = []
        for line in f:
            string = line.strip().split(",")
            for item in string:
                items = item.split("-")
                tmp.append((int(items[0]),int(items[1])))
            myList.append(tmp)
            tmp = []
    return myList

def checkInside(area1, area2):
    if (int(area1[0]) <= int(area2[0])) and (int(area1[1]) <= int(area2[1])):
        print("1: ",area1,"-",area2)
        return False
    elif (int(area2[0]) <= int(area1[0])) and (int(area2[1]) >= int(area1[1])):
        print("2: ", area1[0], "-", area2[0])
        return False
    return True

def checkInside2(area1, area2):
    area1_range = range(area1[0],area1[1]+1)
    area2_range = range(area2[0], area2[1]+1)
    if area2[0] in area1_range or area2[1] in area1_range:
        return False
    elif area1[0] in area2_range or area1[1] in area2_range:
        return False
    return True

def main(liste):
    sum = 0
    for item in liste:
        if not checkInside2(item[0], item[1]):
            sum += 1
    return sum


file = sys.argv[1]
liste = lese(file)
res = main(liste)
print(res)