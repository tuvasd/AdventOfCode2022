import sys
import copy

last_change = 0

def lese(filename):
    list_of_cal = []
    with open(filename) as f:
        sum_current = 0
        for line in f:
            line = line.strip()
            if line == "":
                list_of_cal.append(sum_current)
                sum_current = 0
            else:
                sum_current += int(line)
    list_of_cal.append(sum_current)
    return list_of_cal

def part1(liste):
    print(max(liste))

def part2(liste):
    liste.sort(reverse=True)
    print(sum(liste[:3]))


file = sys.argv[1]
part2(lese(file))
