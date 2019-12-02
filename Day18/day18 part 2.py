# Tips
#   Know how to write DFS and BFS from memory
#   Calculate the total search space.  If for example it's 13! then no amount
#   of code tuning will help.
#   For large search space you need to either prune the tree,  or cache previous
#   results.
#   Remove any optimasations which only give a small gain as they could interfer
#   which caching and break logic

from collections import defaultdict
from dataclasses import dataclass
from typing import List, Set
import networkx as nx

@dataclass(frozen=True, eq=True)
class Location:
  x: int
  y: int

def solve(filename: str) -> int:
  print(f"Solving {filename}....")
  rows = open(filename).read().splitlines()
  dirs = [(-1,0),(1,0),(0,-1),(0,1)]
  
  doors = {}
  keys = {}
  current_locations = []

  G = nx.Graph()
  for row_number, row in enumerate(rows):
    for column_number, cell in enumerate(row):
      if cell != "#":
        G.add_node(Location(column_number, row_number))
        if cell.isupper():
          doors[cell] = Location(column_number, row_number)
        if cell == "@":
          current_locations.append(Location(column_number, row_number))
        if cell.islower():
          keys[cell] = Location(column_number, row_number)

        for off_x, off_y in dirs:
          x = column_number + off_x
          y = row_number + off_y
          if (0 <= x < len(row)) and (0 <= y < len(rows)):
            other_cell = rows[y][x]
            if other_cell != "#":
              G.add_edge(Location(column_number, row_number),Location(x,y), weight=1)

  # The graph has no cycles (other than in the center) this means that from
  # any key there can only be one path to each of the other keys 
  # cycle = nx.find_cycle(G, orientation="original")

  dependencies = defaultdict(list)

  sources = list(keys.items())
  for loc, current_location in enumerate(current_locations):
    sources.insert(0, (str(loc), current_location))
    
  for src_key, source in sources:
    paths = nx.shortest_path(G, source, weight="weight")
    for tar_key, target in keys.items():
      if tar_key != src_key and target in paths:
        path = paths[target]
        
        depends_on = set()
        for door, door_loc in doors.items():
          if (door.lower() != src_key) and (door_loc in path):
            depends_on.add(door.lower())

        for key, key_loc in keys.items():
          if (key != src_key) and (key != tar_key) and (key_loc in path):
            depends_on.add(key)

        dependencies[source].append((tar_key, target, depends_on, len(path)-1))

  cache = {}
  def walk(current_locations: List[Location], collected_keys: Set[str], distance_walked: int):

    # Have we collected all the keys?
    if len(collected_keys) == len(keys):
      return distance_walked

    cache_key = tuple(sorted(collected_keys)), tuple(current_locations)
    if cache_key in cache:
      return cache[cache_key] + distance_walked

    # Where can we get to?
    shortest = 10000
    for i, current_location in enumerate(current_locations):
      new_locations = current_locations.copy()
      targets = dependencies[current_location]
      for (tar_key, tar_loc, depends_on, distance) in targets:
        if tar_key not in collected_keys:
          if depends_on.issubset(collected_keys):
            collected_keys.add(tar_key)
            new_locations[i] = tar_loc
            shortest = min(shortest, walk(new_locations, collected_keys, distance_walked+distance))
            collected_keys.remove(tar_key)

    # Cache the shortest distance from here to the end
    cache[cache_key] = shortest - distance_walked
    return shortest

  return walk(current_locations, set(), 0)

assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample1.txt") == 8
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample2.txt") == 86
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample3.txt") == 132
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample5.txt") == 81
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample4.txt") == 136
assert solve(r"C:\Personal\AdventOfCode2019\Day18\data.txt") == 5068

assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample1_part2.txt") == 8
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample2_part2.txt") == 24
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample3_part2.txt") == 32
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample4_part2.txt") == 72
assert solve(r"C:\Personal\AdventOfCode2019\Day18\data part 2.txt") == 1966