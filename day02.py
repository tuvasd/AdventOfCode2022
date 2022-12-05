import sys
import copy


def lese(filename):
    with open(filename) as f:
        myList = [(list(line.strip().split())) for line in f]
    return myList

def paper(answer):
    if answer == "Z":
        return 3 + 6
    elif answer == "Y":
        return 3 + 2
    elif answer == "X":
        return 1

def rock(answer):
    #Win
    if answer == "Y":
        return 6 + 2
    #draw
    elif answer == "X":
        return 3 + 1
    #Lose
    elif answer == "Z":
        return 3

def scissor(answer):
    #Win
    if answer == "X":
        return 6 + 1
    #draw
    elif answer == "Z":
        return 3 + 3
    #Lose
    elif answer == "Y":
        return 2

def draw(elf):
    if elf == "A":
        return 3+1
    elif elf == "B":
        return 2+3
    elif elf == "C":
        return 3+3

def win(elf):
    if elf == "A":
        return 2+6
    elif elf == "B":
        return 3+6
    elif elf == "C":
        return 1+6 

def lose(elf):
    if elf == "A":
        return 3
    elif elf == "B":
        return 1
    elif elf == "C":
        return 2

def part2(liste):
    score = 0 
    for item in liste:
        if item[1] == "X":
            score += lose(item[0])
        elif item[1] == "Y":
            score += draw(item[0])
        elif item[1] == "Z":
            score += win(item[0])
    print("part 2: ",score)


def main(file):
    liste = lese(file)
    score = 0
    for item in liste:
        if item[0] == "A":
            score += rock(item[1])
        elif item[0] == "B":
            score += paper(item[1])
        elif item[0] == "C":
            score += scissor(item[1])
    print(score)


file = sys.argv[1]
liste = lese(file)
part2(liste)