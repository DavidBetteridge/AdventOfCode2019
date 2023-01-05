from typing import Set
from copy import deepcopy

with open("Day24/data.txt") as f:
  rows = [list(r) for r in f.read().splitlines()]
  bugs = set()
  i=0
  for row in rows:
    for cell in row:
      i+=1
      if cell == "#":
        bugs.add((i, 0))

links = {
  1: [(2,0),(6,0)],
  2: [(1,0),(3,0), (7,0)],
  3: [(2,0),(4,0), (8,0)],
  4: [(3,0),(5,0), (9,0)],
  5: [(4,0), (10,0)],
  6: [(1,0), (7,0), (11,0)],
  7: [(2,0), (6,0), (8,0), (12,0)],
  8: [(3,0), (7,0), (9,0), (13,0)],
  9: [(4,0), (8,0), (10,0), (14,0)],
  10: [(5,0), (9,0), (15,0)],
  11: [(6,0), (12,0), (16,0)],
  12: [(7,0), (11,0), (13,0), (17,0)],
  13: [(8,0), (12,0), (14,0), (18,0)],
  14: [(9,0), (13,0), (15,0), (19,0)],
  15: [(10,0), (14,0), (20,0)],
  16: [(11,0), (17,0), (21,0)],
  17: [(12,0), (16,0), (18,0), (22,0)],
  18: [(13,0), (17,0), (19,0), (23,0)],
  19: [(14,0), (18,0), (20,0), (24,0)],
  20: [(15,0), (19,0), (25,0)],
  21: [(16,0), (22,0)],
  22: [(17,0), (21,0), (23,0)],
  23: [(18,0), (22,0), (24,0)],
  24: [(19,0), (23,0), (25,0)],
  25: [(20,0), (24,0)]
}

def mutate(depth: int, bugs: Set[str]) -> Set[str]:
  temp = deepcopy(bugs)

  for bug_number in range(1, 26):
    bug_count = 0
    for link in links[bug_number]:
      if link in bugs:
        bug_count+=1
    if ((bug_number,depth) in bugs) and bug_count != 1:
      # bug dies
      temp.remove((bug_number,depth))
    elif ((bug_number,depth) not in bugs) and bug_count in [1,2]:
      # infested
      temp.add((bug_number,depth))
  return temp

def print_rows(bugs: Set[str]):
  for bug_number in range(1, 26):
    if bug_number % 5 == 1:
      print()
    if (bug_number,0) in bugs:
      print("#",end="")
    else:
      print(".",end="")
  print("")

def biodiversity_rating(bugs: Set[str]):
  rating = 0
  for bug_number in range(1, 26):
    if (bug_number,0) in bugs:
      rating += (2 ** (bug_number-1))
  return rating

seen = set()
while True:
  bugs = mutate(0, bugs)
  rating = biodiversity_rating(bugs)
  if rating in seen:
    print_rows(bugs)
    print(rating)
    break
  else:
    seen.add(rating)
