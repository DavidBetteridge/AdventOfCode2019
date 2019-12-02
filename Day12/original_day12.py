import re

class Moon:
    def __init__(self, x, y, z):
        self.initialX = x
        self.initialY = y
        self.initialZ = z        
        self.positionX = x
        self.positionY = y
        self.positionZ = z
        self.velocityX = 0
        self.velocityY = 0
        self.velocityZ = 0

    def __repr__(self):
        return f'position={self.positionX},{self.positionY},{self.positionZ} velocity={self.velocityX},{self.velocityY},{self.velocityZ}'

    def potential_energy(self):
        return abs(self.positionX) + abs(self.positionY) + abs(self.positionZ)

    def kinetic_energy(self):
        return abs(self.velocityX) + abs(self.velocityY) + abs(self.velocityZ)


def update_moons():
    for m1 in range(len(moons) - 1):
        for m2 in range(m1 + 1, len(moons)):
            moon1 = moons[m1]  
            moon2 = moons[m2]  

            # Apply Gravity
            if moon1.positionX > moon2.positionX:
                moon2.velocityX += 1
                moon1.velocityX -= 1

            if moon1.positionX < moon2.positionX:
                moon2.velocityX -= 1
                moon1.velocityX += 1

            if moon1.positionY > moon2.positionY:
                moon2.velocityY += 1
                moon1.velocityY -= 1

            if moon1.positionY < moon2.positionY:
                moon2.velocityY -= 1
                moon1.velocityY += 1

            if moon1.positionZ > moon2.positionZ:
                moon2.velocityZ += 1
                moon1.velocityZ -= 1

            if moon1.positionZ < moon2.positionZ:
                moon2.velocityZ -= 1
                moon1.velocityZ += 1

    # Apply Velocity
    for moon in moons:        
        moon.positionX += moon.velocityX
        moon.positionY += moon.velocityY
        moon.positionZ += moon.velocityZ    

pattern = re.compile(r'\<x=(?P<x>\-*[0-9]+), y=(?P<y>\-*[0-9]+), z=(?P<z>\-*[0-9]+)\>')
moons = []
for line in open('Day12/day12.txt').read().splitlines():
    match = pattern.match(line)
    moons.append(Moon(int(match.group("x")), int(match.group("y")), int(match.group("z"))))


steps = 0
last = 0
while True:
    steps += 1
    update_moons()

    if moons[0].positionY ==  moons[0].initialY and moons[0].velocityY == 0:
        print(f'{steps} {steps-last}')
        last = steps


def part_one():
    total_energy = sum([ moon.potential_energy() * moon.kinetic_energy() for moon in moons])
    print(total_energy)

#part_one()

def generate_sequence(increments):
    increment = 0
    step = 0

    while True:
        step += increments[increment]
        increment = (increment + 1) % len(increments)
        yield step

moon0x = generate_sequence([114, 223,8, 38, 59713, 41236, 59713, 38, 8, 223, 114])
moon0y = generate_sequence([9, 1684, 20467, 19255, 148784, 19255, 20467, 1684, 9])
for x in [next(moon0x) for _ in range(100)]:
    print(x)





# X
# 0   0
# 114 114
# 337 223
# 345 8
# 383 38
# 60096 59713
# 101332 41236
# 161045 59713
# 161083 38
# 161091 8
# 161314 223
# 161428 114

# Y
# 231614 9
# 231623 9
# 233307 1684
# 253774 20467
# 273029 19255
# 421813 148784
# 441068 19255
# 461535 20467
# 463219 1684

# Z
# 102294 102232
# 102343 49
# 102356 13
# 102369 13
# 102418 49