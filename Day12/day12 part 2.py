import re
from typing import List
from dataclasses import dataclass
from itertools import combinations
from copy import deepcopy
from math import lcm

X = int
Y = int
Z = int
Position = List[int]
Velocity = List[int]

@dataclass
class Moon:
  position: Position
  velocity: Velocity

with open(f"C:\Personal\AdventOfCode2019\Day12\data.txt") as f:
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

# We can consider x,y and z independently.  We count the number of steps it takes
# x to repeat,  y to repeat and z to repeat.  We then want when they first all repeat
# at the same time so we take their lcm
base = deepcopy(moons)
solutions = [None,None,None]
def duplicates_to_be_found(moons, base, steps):
  for dim in range(3):
    if (    moons[0].position[dim] == base[0].position[dim] 
        and moons[1].position[dim] == base[1].position[dim]
        and moons[2].position[dim] == base[2].position[dim]
        and moons[3].position[dim] == base[3].position[dim]
        and moons[0].velocity[dim] == base[0].velocity[dim] 
        and moons[1].velocity[dim] == base[1].velocity[dim]
        and moons[2].velocity[dim] == base[2].velocity[dim]
        and moons[3].velocity[dim] == base[3].velocity[dim]):
      if solutions[dim] is None:
        solutions[dim] = steps
        print(f"Dim {dim} took {steps} steps to repeat")
  return solutions[0] is None or solutions[1] is None or solutions[2] is None

steps = 0
while (steps < 1 or duplicates_to_be_found(moons, base, steps)):
  for moon1, moon2 in combinations(moons, 2):
    for dimension in range(3):
      if moon1.position[dimension] < moon2.position[dimension]:
        moon1.velocity[dimension] += 1
        moon2.velocity[dimension] -= 1
      elif moon1.position[dimension] > moon2.position[dimension]:
        moon1.velocity[dimension] -= 1
        moon2.velocity[dimension] += 1
  steps +=1

  for moon in moons:
    for dimension in range(3):
      moon.position[dimension] += moon.velocity[dimension]

part2 = lcm(*solutions)
print(part2)
assert part2 == 478373365921244
