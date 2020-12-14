import re

class Moon:
    def __init__(self, x, y, z):
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


pattern = re.compile(r'\<x=(?P<x>\-*[0-9]+), y=(?P<y>\-*[0-9]+), z=(?P<z>\-*[0-9]+)\>')
moons = []
for line in open('Day12/day12.txt').read().splitlines():
    match = pattern.match(line)
    moons.append(Moon(int(match.group("x")), int(match.group("y")), int(match.group("z"))))

for step in range(1000):
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

total_energy = sum([ moon.potential_energy() * moon.kinetic_energy() for moon in moons])
print(total_energy)

