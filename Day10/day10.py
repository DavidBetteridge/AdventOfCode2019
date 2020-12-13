import math

field = open('Day10/day10.txt').read().splitlines()
rows = len(field)
columns = len(field[0])

def visible_from_location(oX, oY):
    slopes = set()
    for x in range(columns):
        for y in range(rows):
            if (x != oX or y != oY) and field[y][x] == '#':
                xDiff = x - oX
                yDiff = y - oY
                theta = math.atan2(yDiff, xDiff)
                slopes.add(theta)

    return len(slopes)

def part_one():
    return max([visible_from_location(oX, oY) for oX in range(columns) for oY in range(rows) if field[oY][oX] == '#'])