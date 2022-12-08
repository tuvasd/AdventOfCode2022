import sys
import copy


def lese(filename):
    with open(filename) as f:
        myList = [(list(line.strip().split())) for line in f]
    return myList


def doCommands(commands):
    current_path = []
    current_node = "root"
    directory = {}
    contains_below = []

    nr_command = 1

    while nr_command < len(commands):
        command = commands[nr_command]

        if "ls" in command:
            nr_command += 1
            con = True

            while con:
                if nr_command < len(commands):
                    command = commands[nr_command]

                    if "cd" in command:
                        con = False
                    else:
                        contains_below.append(command)
                        nr_command += 1
                else:
                    con = False
            node_path = ""
            for node in current_path:
                node_path += "/" + node
            node_path += "/" + current_node
            size, folder_below = buildedic(contains_below, directory, node_path)
            directory[node_path] = [node_path, size, folder_below]
            contains_below = []

        elif "cd" in command:
            if ".." in command:
                current_node = current_path.pop()
            else:
                current_path.append(current_node)
                current_node = command[2]
            nr_command += 1

    return directory


def buildedic(commands, directory, path):
    size = 0
    contains = []
    for item in commands:
        if item[0].isnumeric():
            size += int(item[0])
        contains.append([item[1], item[0]])
    paths = path.split("/")
    add_path = ""
    for node in paths[1:]:
        add_path += "/" + node
        if add_path in directory:
            directory[add_path][1] += size
    return size, contains


def sumDir(directory):
    sum = 0
    for key in directory:
        size = directory[key][1]
        if size < 100000:
            sum += size
    return sum


def part2(directory):
    neededspace = abs(70000000 - 30000000 - directory["/root"][1])

    current_size = directory["/root"][1]
    current_select = "/root"

    for key in directory:
        size = directory[key][1]
        if neededspace < size < current_size:
            current_select = key
            current_size = size
    print(current_select, " - ", current_size)


file = sys.argv[1]
commands = lese(file)
directory = doCommands(commands)

part1 = sumDir(directory)
print("Part 1: ",part1)

part2(directory)
