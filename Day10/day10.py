import math
import sys

field = list(map(list, open('Day10/day10.txt').read().splitlines()))
rows = len(field)
columns = len(field[0])

def visible_from_location(oX, oY):
    slopes = {}
    for x in range(columns):
        for y in range(rows):
            if (x != oX or y != oY) and field[y][x] == '#':
                xDiff = x - oX
                yDiff = y - oY
                distance = (xDiff * xDiff) + (yDiff * yDiff)
                theta = math.atan2(yDiff, xDiff)

                if theta in slopes:
                    _, _, current = slopes[theta]
                    if current > distance:
                        slopes[theta] = (x, y, distance)
                else:
                    slopes[theta] = (x, y, distance)
    return slopes

def part_one():
    return max([(len(visible_from_location(oX, oY)),oX, oY) for oX in range(columns) for oY in range(rows) if field[oY][oX] == '#'])

print(part_one())

oX = 20
oY = 19

# oX = 11
# oY = 13
laserAngle = (-math.pi/2) - sys.float_info.epsilon

for _ in range(200):
    slopes = visible_from_location(oX, oY)
    slopesInOrder = sorted(slopes.keys())

    inLine = [s for s in slopesInOrder if s > laserAngle]
    if len(inLine) == 0:
        inLine = [s for s in slopesInOrder if s > -math.pi]

    nextSlope = next(iter(inLine))
    x, y, _ = slopes[nextSlope]
    field[y][x] = "."

    print(slopes[nextSlope])
    laserAngle = nextSlope

#404    