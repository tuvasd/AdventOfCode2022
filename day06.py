import sys
import re

def lese(filename):
    with open(filename) as f:
        return f.readline()

def unique(s):
    return len(set(s)) == len(s)

def main(s, start, stop):
    while True:
        if unique(s[start:stop]):
            print(stop)
            break
        start += 1
        stop += 1

file = sys.argv[1]
string = lese(file)
#part 1
main(string,0,4)

#part 2
main(string,0,14)
