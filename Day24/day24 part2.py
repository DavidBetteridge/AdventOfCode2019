from typing import Set

with open("Day24/data.txt") as f:
  bugs = set()
  i=0
  for row in [list(r) for r in f.read().splitlines()]:
    for cell in row:
      i+=1
      if cell == "#":
        bugs.add((i, 0))

# W N E S
links = {
  1: [(12,-1), (8,-1), (2,0), (6,0)],
  2: [(1,0), (8,-1), (3,0), (7,0)],
  3: [(2,0), (8,-1),(4,0), (8,0)],
  4: [(3,0), (8,-1),(5,0), (9,0)],
  5: [(4,0), (8,-1),(14,-1), (10,0)],
  6: [(12,-1), (1,0), (7,0), (11,0)],
  7: [(2,0), (6,0), (8,0), (12,0)],
  8: [(3,0), (7,0), (9,0), (1,1), (2,1), (3,1), (4,1), (5,1)],
  9: [(4,0), (8,0), (10,0), (14,0)],
  10: [(5,0), (9,0),(14,-1), (15,0)],
  11: [(12,-1), (6,0), (12,0), (16,0)],
  12: [(11,0), (7,0), (1,1),(6,1),(11,1),(16,1),(21,1), (17,0)],
  14: [(5,1),(10,1),(15,1),(20,1),(25,1), (9,0), (15,0), (19,0)],
  15: [(14,0), (10,0),(14,-1), (20,0)],
  16: [(12,-1), (11,0), (17,0), (21,0)],
  17: [(16,0), (12,0), (18,0), (22,0)],
  18: [(17,0), (21,1), (22,1), (23,1), (24,1), (25,1), (19,0), (23,0)],
  19: [(18,0), (14,0), (20,0), (24,0)],
  20: [(19,0), (15,0),(14,-1), (25,0)],
  21: [(12,-1), (16,0), (22,0), (18,-1)],
  22: [(21,0), (17,0), (23,0), (18,-1)],
  23: [(22,0), (18,0), (24,0), (18,-1)],
  24: [(23,0), (19,0), (25,0), (18,-1)],
  25: [(24,0), (20,0),(14,-1) ,(18,-1)]
}

def mutate(bugs: Set[str]) -> Set[str]:
  min_depth = min(d for _,d in bugs)
  max_depth = max(d for _,d in bugs)

  temp = bugs.copy()
  for depth in range(min_depth-1, max_depth+2):
    for bug_number in range(1, 26):
      if bug_number != 13:
        bug_count = sum([1 for i,d_off in links[bug_number]
                        if (i,depth+d_off) in bugs])
        bug_is_alive = (bug_number,depth) in bugs

        if bug_is_alive and bug_count != 1:
          # bug dies
          temp.remove((bug_number,depth))
        elif (not bug_is_alive) and bug_count in [1,2]:
          # infested
          temp.add((bug_number,depth))
  return temp

for minute in range(200):
  bugs = mutate(bugs)
print(len(bugs))
