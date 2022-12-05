import sys
import copy


def lese1(filename):
    with open(filename) as f:
        myList = []
        for line in f:
            string = line.strip()
            length = int(len(string) / 2)
            myList.append((string[:length], string[length:]))
    return myList


def lese2(filename):
    with open(filename) as f:
        myList = []
        tmp = []
        counter = 0
        for line in f:
            line = line.strip()
            if counter > 2:
                myList.append(tmp)
                tmp = []
                counter = 0
            tmp.append(line)
            counter += 1

        myList.append(tmp)
        #print(myList)
    return myList


def match(sub1, sub2, sub3):
    common_characters = ''.join(set(sub1).intersection(sub2))
    common_characters2 = "".join(set(common_characters).intersection(sub3))
    return common_characters2


def calc(word):
    sum = 0
    for char in word:
        if char.isupper():
            sum += ord(char) - 38
        else:
            sum += ord(char) - 96
    return sum


def main(liste):
    common_list = []
    sum = 0
    for item in liste:
        com = match(item[0], item[1], item[2])
        sum += calc(com)
    print(sum)


file = sys.argv[1]
liste = lese2(file)
main(liste)
