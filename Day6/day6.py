orbits = {}
orbitting = {}
for line in open('Day6/day6.txt').read().splitlines():
    lhs, rhs = line.split(')')

    if lhs in orbits:
        orbits[lhs].append(rhs)
    else:
        orbits[lhs] = [rhs]

    orbitting[rhs] = lhs

counts = {}
counts['COM'] = 0
def workout_counts(baseLocation):
    for o in orbits[baseLocation]:
        counts[o] = counts[baseLocation] + 1
        if o in orbits:
            workout_counts(o)

def calculate_distance_to_com(startFrom):
    travelled = {}
    current = startFrom
    distance = 0
    while current != "COM":
        travelled[current] = distance
        current = orbitting[current]
        distance += 1
    return travelled        

def part_one():
    workout_counts('COM')
    return sum(counts.values())

def part_two():
    fromYou = calculate_distance_to_com('YOU')
    fromSan = calculate_distance_to_com('SAN')

    join = next(iter([o for o in fromYou if o in fromSan]))
    return fromYou[join] + fromSan[join] - 2