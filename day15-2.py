import sys
import re


class Sensor:
    def __init__(self, sensor, beacon):
        self.x = sensor[0]
        self.y = sensor[1]
        self.beaconX = beacon[0]
        self.beaconY = beacon[1]
        self.manhattenDis = self.manhatten()
        self.param = self.setParameter()

    def manhatten(self):
        # print("X: ", self.x, " - ", self.beaconX)
        # print("Y: ", self.y, " - ", self.beaconY)
        # print(abs(self.x - self.beaconX) + abs(self.y - self.beaconY))
        return abs(self.x - self.beaconX) + abs(self.y - self.beaconY)

    def setParameter(self):
        # print("Making param")
        param = set()
        sx = self.x
        sy = self.y
        d = self.manhattenDis
        moving = [(-1, 1), (1, -1), (-1, -1), (1, 1)]
        for dx in range(d + 2):
            dy = (d + 1) - dx
            for mx, my in moving:
                x, y = sx + (dx * mx), sy + (dy * my)
                if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                    continue
                param.add((x, y))
        return param

    def __str__(self):
        return f"Sensor at: {self.x}, {self.y} Beacon at: {self.beaconX}, {self.beaconY} Manhatten Distanse is {self.manhattenDis} and Param is {len(self.param)} "

def lese(filename):
    myList = []
    tmp = []
    with open(filename) as f:
        for line in f:
            numbers = re.findall(r'[-+]?\d+', line)
            tmp.append(numbers)
        for item in tmp:
            myList.append([(int(item[0]), int(item[1])), (int(item[2]), int(item[3]))])
    return myList


def manhattenDis(sensors, x, y):
    for sensor in sensors:
        dist = abs(x - sensor.x) + abs(y - sensor.y)
        if dist <= sensor.manhattenDis:
            return False
    return True


def findPoint(sensors):
    cnt = 1
    for sensor in sensors:
        print(cnt)
        cnt += 1
        for x,y in sensor.param:
            res = manhattenDis(sensors, x,y)
            if res:
                print(x,y)
                print(x * 4000000 + y)
                return x * 4000000 + y

def part2(input):
    sensors = []
    cnt = 1
    beacons = set()
    for sensor, beacon in input:
        beacons.add(beacon)
        sensors.append(Sensor(sensor, beacon))
        print(cnt)
        cnt += 1

    point = findPoint(sensors)
    print(point)

file = sys.argv[1]
input = lese(file)
part2(input)
