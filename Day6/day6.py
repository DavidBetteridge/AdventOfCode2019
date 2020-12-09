orbits = {}

for line in open('Day6/day6.txt').read().splitlines():
    lhs, rhs = line.split(')')

    if lhs in orbits:
        orbits[lhs].append(rhs)
    else:
        orbits[lhs] = [rhs]


counts = {}
counts['COM'] = 0

def workout_counts(baseLocation):
    for o in orbits[baseLocation]:
        counts[o] = counts[baseLocation] + 1
        if o in orbits:
            workout_counts(o)

workout_counts('COM')
print (sum(counts.values()))

