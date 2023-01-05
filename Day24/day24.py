from typing import List
from copy import deepcopy

with open("Day24/data.txt") as f:
  rows = [list(r) for r in f.read().splitlines()]

def mutate(rows: List[str]) -> List[str]:
  temp = deepcopy(rows)
  for row_number, row in enumerate(rows):
    for column_number, cell in enumerate(row):
      bug_count = 0
      for x_off, y_off in [(-1,0),(1,0),(0,-1),(0,1)]:
        x = column_number+x_off
        y = row_number+y_off
        if (0 <= x < len(row)) and (0 <= y < len(rows)) and (rows[y][x] == "#"):
          bug_count+=1
      
      if cell == '#' and bug_count != 1:
        # bug dies
        temp[row_number][column_number]="."
      elif cell == "." and bug_count in [1,2]:
        # infested
        temp[row_number][column_number]="#"
  return temp

def print_rows(rows: List[str]):
  for row in rows:
    print(row)

def biodiversity_rating(rows: List[str]):
  p = 0
  rating = 0
  for row in rows:
    for cell in row:
      if cell == "#":
        rating += (2 ** p)
      p+=1
  return rating

seen = set()
rating = biodiversity_rating(rows)
while True:
  rows = mutate(rows)
  rating = biodiversity_rating(rows)
  if rating in seen:
    print_rows(rows)
    print(rating)
    break
  else:
    seen.add(rating)
