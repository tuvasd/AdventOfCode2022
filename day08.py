import sys

def lese(filename):
    forest = []
    with open(filename) as f:
        myList = [(list(list(line.strip()))) for line in f]
        for line in myList:
            res = [eval(i) for i in line]
            forest.append(res)
    return forest

def countOutside(forest):
    return (len(forest) + len(forest[0]))-1 + (len(forest)-1 + len(forest[0])-2)
def checkList(treeList, tree):
    return all(i < tree for i in treeList)

def checkScore(treelist,tree):
    counter = 1
    for score in treelist:
        if counter == len(treelist):
            return counter
        elif score < tree:
            counter += 1
        else: break
    return counter
def countInside(forest):
    nr_visible = 0
    for i in range(1,len(forest)-1):
        for j in range(1,len(forest[0])-1):
            treeValue = forest[i][j]
            list_left = checkList(forest[i][:j],treeValue)
            list_rigth = checkList(forest[i][j+1:],treeValue)
            list_up = checkList([i[j] for i in forest[:i]], treeValue)
            list_down = checkList([i[j] for i in forest[i+1:]], treeValue)
            if list_left or list_rigth or list_up or list_down:
                nr_visible += 1
    return nr_visible

def scenicCounter(forest):
    nr_visible = 0
    res = []
    for i in range(1,len(forest)-1):
        for j in range(1,len(forest[0])-1):
            treeValue = forest[i][j]
            list_left = checkScore(forest[i][:j][::-1],treeValue)
            list_rigth = checkScore(forest[i][j+1:],treeValue)
            list_up = checkScore([i[j] for i in reversed(forest[:i])], treeValue)
            list_down = checkScore([i[j] for i in forest[i+1:]], treeValue)
            res_tree = list_up * list_down * list_rigth * list_left
            res.append(res_tree)
    return int(max(res))

def part1(forest):
    nr_visible = countOutside(forest)
    nr_visible += countInside(forest)
    print(nr_visible)

def part2(forest):
    value = scenicCounter(forest)
    print(value)


file = sys.argv[1]
forest = lese(file)
part2(forest)

