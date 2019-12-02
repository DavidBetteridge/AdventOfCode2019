# Movement commands - north (1), south (2), west (3), and east (4)
# The repair droid can reply with any of the following status codes:

# 0: The repair droid hit a wall. Its position has not changed.
# 1: The repair droid has moved one step in the requested direction.
# 2: The repair droid has moved one step in the requested direction;
#       its new position is the location of the oxygen system.

import networkx as nx
from Computer import Computer


# Load the program
text = open('Day15/data.txt').read()
s = text.split(',')
memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])

G = nx.Graph()
path = []
current_location = (0,0)
oxygen = (0,0)
droid = (0,0)
next_move = (0,0)
known = {}
known[current_location] = "D"
backtrack = False

def print_map():
  for r in range(-30,30):
    for c in range(-30, 30):
      print(known.get((c,r)," "), end="")
    print("")

def read_from_keyboard():
  global current_location
  global next_move
  global backtrack
  
  # North
  next_move = (current_location[0], current_location[1]-1)
  if next_move not in known:
    backtrack = False
    return 1

  # South
  next_move = (current_location[0], current_location[1]+1)
  if next_move not in known:
    backtrack = False
    return 2

  # West
  next_move = (current_location[0]-1, current_location[1])
  if next_move not in known:
    backtrack = False
    return 3

  # East
  next_move = (current_location[0]+1, current_location[1])
  if next_move not in known:
    backtrack = False
    return 4

  # Step back
  if len(path) == 0:
    print_map()
  else:
    backtrack = True
    next_move = path.pop()
    if next_move[1] < current_location[1]:
      return 1
    elif next_move[1] > current_location[1]:
      return 2
    elif next_move[0] < current_location[0]:
      return 3
    elif next_move[0] > current_location[0]:
      return 4
  
  # Graph should now be built
  print(oxygen, droid)
  print(len(nx.shortest_path(G, droid, oxygen))-1)
  return -1

def output_to_screen(valueToPrint):
  global current_location
  global oxygen

  if valueToPrint == 0:
    # Hit a wall.
    known[next_move]="#"

  elif valueToPrint == 1:
    if not backtrack: 
      G.add_edge(current_location, next_move)
      path.append(current_location)
    current_location = next_move
    if next_move not in known:
      known[next_move]="."

  elif valueToPrint == 2:
    if not backtrack: 
      path.append(current_location)
      G.add_edge(current_location, next_move)
    current_location = next_move
    oxygen = current_location
    known[next_move]="O"

com = Computer(memory)

com.run_program(read_from_keyboard, output_to_screen)

