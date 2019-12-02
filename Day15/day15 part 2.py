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
  minX = min(known, key=lambda a: a[0])[0]
  minY = min(known, key=lambda a: a[1])[1]
  maxX = max(known, key=lambda a: a[0])[0]
  maxY = max(known, key=lambda a: a[1])[1]

  for r in range(minX,maxX+1):
    for c in range(minY, maxY+1):
      print(known.get((c,r)," "), end="")
    print("")


def fill_with_oxygen():

  def read_oxygen(value:str):
    if  isinstance(value, int):
      return value
    else:
      return 99999

  minX = min(known, key=lambda a: a[0])[0]
  minY = min(known, key=lambda a: a[1])[1]
  maxX = max(known, key=lambda a: a[0])[0]
  maxY = max(known, key=lambda a: a[1])[1]
  max_level = 0
  work = True
  while work:
    work = False
    for r in range(minX,maxX+1):
      for c in range(minY, maxY+1):
        # If cell is . or D and is next to a number,  then make it the lowest
        # number plus one.
        if known.get((c,r)," ") == ".":
          level = min( read_oxygen(known.get((c,r-1)," ")),
                      read_oxygen(known.get((c,r+1)," ")),
                      read_oxygen(known.get((c-1,r)," ")),
                      read_oxygen(known.get((c+1,r)," "))
                      )
          if level != 99999:
            known[(c,r)] = level+1
            max_level = max(max_level, level+1)
            work = True
    print(max_level) #290

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
  fill_with_oxygen()
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
    known[next_move]=0

com = Computer(memory)

com.run_program(read_from_keyboard, output_to_screen)

