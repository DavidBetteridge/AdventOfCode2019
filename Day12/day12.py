import re
from typing import List
from dataclasses import dataclass
from itertools import combinations

X = int
Y = int
Z = int
Position = List[int]
Velocity = List[int]

@dataclass
class Moon:
  position: Position
  velocity: Velocity

  def __str__(self) -> str:
    return f"pos=<x= {self.position[0]}, y={self.position[1]}, z= {self.position[2]}>, vel=<x= {self.velocity[0]}, y={self.velocity[1]}, z={self.velocity[2]}>"

  def potential(self):
    return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

  def kinetic(self):
    return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

with open("Day12/data.txt") as f:
  lines = f.read().splitlines()

  pattern = re.compile(r"<x=(?P<x>-?[0-9]+), y=(?P<y>-?[0-9]+), z=(?P<z>-?[0-9]+)>") 
  moons = []
  for line in lines:
    matches = re.match(pattern, line)
    pos_x = int(matches.group("x"))
    pos_y = int(matches.group("y"))
    pos_z = int(matches.group("z"))
    pos = [pos_x, pos_y, pos_z]
    vel = [0,0,0]
    moons.append(Moon(pos,vel))

for step in range(1000):
  for moon1, moon2 in combinations(moons, 2):
    for dimension in range(3):
      if moon1.position[dimension] < moon2.position[dimension]:
        moon1.velocity[dimension] += 1
        moon2.velocity[dimension] -= 1
      elif moon1.position[dimension] > moon2.position[dimension]:
        moon1.velocity[dimension] -= 1
        moon2.velocity[dimension] += 1

  for moon in moons:
    for dimension in range(3):
      moon.position[dimension] += moon.velocity[dimension]

part1 = sum(moon.potential() * moon.kinetic() for moon in moons)
print(part1)