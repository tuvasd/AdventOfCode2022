import sys
import re

class Sensor:
    def __init__(self, sensor, beacon):
        self.x = sensor[0]
        self.y = sensor[1]
        self.beaconX = beacon[0]
        self.beaconY = beacon[1]
        self.relevant = False
        self.relevantGrid = []
        self.manhattenDis = self.manhatten()
        self.param = self.setParameter()


    def manhatten(self):
        return abs(self.x-self.beaconX)+abs(self.y-self.beaconY)

    def setParameter(self):
        param = set()
        nextX = self.x - (self.manhattenDis+1)
        nextY = self.y
        moving = [(1,-1),(1,1),(-1,1),(-1,-1)]
        for dir in moving:
            for _ in range(self.manhattenDis+1):
                param.add((nextY,nextX))
                nextX += dir[0]
                nextY += dir[1]
                if nextY == 2000000:
                    self.relevant = True
                    self.relevantGrid.append((nextX,nextY))
        return param

    def __str__(self):
        return f"Sensor at: {self.x}, {self.y} Beacon at: {self.beaconX}, {self.beaconY} Manhatten Distanse is {self.manhattenDis} and Param is {self.param} "


def lese(filename):
    myList = []
    tmp = []
    with open(filename) as f:
        for line in f:
            numbers = re.findall(r'[-+]?\d+', line)
            tmp.append(numbers)
        for item in tmp:
            myList.append([(int(item[0]),int(item[1])),(int(item[2]),int(item[3]))])
    return myList
def count(sensors,number):
    counter = set()
    for sensor in sensors:
        if sensor.relevant:
            param = sensor.relevantGrid
            print(sensor.x,",",sensor.y, "-",param)
            minX = min(param[0][0],param[1][0])+1
            maxX = max(param[0][0],param[1][0])
            for i in range(minX,maxX):
                counter.add(i)
    return counter


def part1(input):
    sensors = []
    cnt = 1
    beacons = set()
    for sensor, beacon in input:
        beacons.add(beacon)
        sensors.append(Sensor(sensor,beacon))
        print(cnt)
        cnt += 1

    #counter = count(sensors,10)
    counter = count(sensors, 2000000)

    for beacon in beacons:
        if beacon[1] == 2000000:
            print(beacon)
            counter.remove(beacon[0])
    print(len(counter))

file = sys.argv[1]
input = lese(file)
part1(input)
