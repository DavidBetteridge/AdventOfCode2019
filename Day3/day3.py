def follow_path(path):
    x = 0
    y = 0
    visited = []
    for step in path.split(','):
        direction = step[0]
        distance = int(step[1:])

        if direction == 'R':
            for _ in range(0, distance):
                x += 1
                visited.append((x,y))

        if direction == 'L':
            for _ in range(0, distance):
                x -= 1
                visited.append((x,y))

        if direction == 'U':
            for _ in range(0, distance):
                y += 1
                visited.append((x,y))

        if direction == 'D':
            for _ in range(0, distance):
                y -= 1
                visited.append((x,y))
    return visited

def calculate_distance(point):
    x, y = point
    return abs(x) + abs(y)

def calculate_cost(location):
    return places1.index(location) + places2.index(location) + 2

def part_one():
    distances = list(map(calculate_distance, common))
    return min(distances)

def part_two():
    costs = list(map(calculate_cost, common))
    return min(costs)

path1, path2 = open('Day3/day3.txt').read().splitlines()
places1 = follow_path(path1)
places2 = follow_path(path2)
common = list(set(places1).intersection(set(places2)))    