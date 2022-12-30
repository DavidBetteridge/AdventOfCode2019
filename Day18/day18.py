from dataclasses import dataclass
from typing import Set
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
  current_location = None
  
  G = nx.Graph()
  for row_number, row in enumerate(rows):
    for column_number, cell in enumerate(row):
      if cell != "#":
        if cell.isupper():
          doors[cell] = Location(column_number, row_number)
        else:
          if cell == "@":
            current_location = Location(column_number, row_number)
          if cell.islower():
            keys[cell] = Location(column_number, row_number)

          for off_x, off_y in dirs:
            x = column_number + off_x
            y = row_number + off_y
            if (0 <= x < len(row)) and (0 <= y < len(rows)):
              other_cell = rows[y][x]
              if other_cell != "#" and not other_cell.isupper():
                G.add_edge(Location(column_number, row_number),Location(x,y))
  best_path_length = 999999
  def walk(current_location: Location, collected_keys: Set[str], distance_walked: int, route: str):
    nonlocal best_path_length
    
    if distance_walked >= best_path_length:
      return distance_walked

    # Have we collected all the keys?
    if len(collected_keys) == len(keys):
      best_path_length = min(best_path_length, distance_walked)
      return distance_walked

    shortest_path = 99999999
    for key,key_loc in keys.items():
      if key not in collected_keys and key_loc in G.nodes() and nx.has_path(G, current_location, key_loc):
        
        # Walk to key
        path = nx.shortest_path(G, current_location, key_loc)[:-1]
        
        # Check we aren't walking past another key
        if is_key_enroute(collected_keys, path):
          continue

        distance = len(path)

        # Collect key
        collected_keys.add(key)

        # Unlock door
        door_loc = None
        if key.upper() in doors:
          door_loc = doors[key.upper()]
          for off_x, off_y in dirs:
            x = door_loc.x + off_x
            y = door_loc.y + off_y
            other_cell = rows[y][x]
            if other_cell != "#" and ((not other_cell.isupper()) or other_cell.lower() in collected_keys):
              G.add_edge(door_loc,Location(x,y))
        shortest_path = min(shortest_path, walk(key_loc, collected_keys, distance_walked+distance, route+f"{key} ({distance})  "))
          
        # Relock door
        if door_loc:
          G.remove_node(door_loc)
      
        # Return key
        collected_keys.remove(key)
    return shortest_path

  def is_key_enroute(collected_keys, path):
    for another_key,another_key_loc in keys.items():
      if (another_key not in collected_keys) and (another_key_loc in path):
        return True
    return False

  return walk(current_location, set(), 0, "")

# print(solve(r"C:\Personal\AdventOfCode2019\Day18\data.txt"))
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample1.txt") == 8
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample2.txt") == 86
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample3.txt") == 132
# assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample4.txt") == 136
assert solve(r"C:\Personal\AdventOfCode2019\Day18\sample5.txt") == 81