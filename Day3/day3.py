path1, path2 = open('Day3/day3.txt').read().splitlines()

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

def part_one():
    places1 = set(follow_path(path1))
    places2 = set(follow_path(path2))
    common = places1.intersection(places2)
    distances = list(map(calculate_distance, common))
    return min(distances)

print(part_one())
