from Computer import Computer

# Load the program
text = open('Day17/data.txt').read()
s = text.split(',')
memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])

def read_from_keyboard():
  return -1

row = 0
column = 0
grid = {}
current_location = ()
def output_to_screen(valueToPrint):
  global row
  global column
  global current_location
  
  if valueToPrint == 10:
    row+=1
    column=0
  else:
    grid[(column, row)] = chr(valueToPrint)
    if chr(valueToPrint) == "^":
      current_location = (column, row)
    column+=1

  print(chr(valueToPrint),end="")

com = Computer(memory)

com.run_program(read_from_keyboard, output_to_screen)


maxX = max(grid, key=lambda x: x[0])[0]
maxY = max(grid, key=lambda x: x[1])[1]

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

commands = []


def turn_left(current_direction):
  commands.append("L")
  return (current_direction - 1) % 4

def turn_right(current_direction):
  commands.append("R")
  return (current_direction + 1) % 4

def turn_to_follow_path(current_direction, current_location):
  if current_direction == NORTH:
    if grid.get((current_location[0]-1, current_location[1]), "?") == "#":
      return turn_left(current_direction)
    elif grid.get((current_location[0]+1, current_location[1]), "?") == "#":
      return turn_right(current_direction)
    else:
      return None
  elif current_direction == SOUTH:
    if grid.get((current_location[0]+1, current_location[1]), "?") == "#":
      return turn_left(current_direction)
    elif grid.get((current_location[0]-1, current_location[1]), "?") == "#":
      return turn_right(current_direction)
    else:
      return None
  elif current_direction == WEST:
    if grid.get((current_location[0], current_location[1]+1), "?") == "#":
      return turn_left(current_direction)
    elif grid.get((current_location[0], current_location[1]-1), "?") == "#":
      return turn_right(current_direction)
    else:
      return None
  elif current_direction == EAST:
    if grid.get((current_location[0], current_location[1]-1), "?") == "#":
      return turn_left(current_direction)
    elif grid.get((current_location[0], current_location[1]+1), "?") == "#":
      return turn_right(current_direction)
    else:
      return None


def walk_to_end_of_path(current_direction, current_location):
  distance = 0
  while True:
    if current_direction == NORTH:
      next_location = (current_location[0], current_location[1]-1)
    elif current_direction == SOUTH:
      next_location = (current_location[0], current_location[1]+1)
    elif current_direction == WEST:
      next_location = (current_location[0]-1, current_location[1])
    elif current_direction == EAST:
      next_location = (current_location[0]+1, current_location[1])

    if (0 <= next_location[0] <= maxX) and \
       (0 <= next_location[1] <= maxY) and \
        grid[next_location] == "#":
      distance+=1
      current_location = next_location
    else:
      break
  commands.append(distance)
  return current_location

current_direction = NORTH
current_direction = turn_left(current_direction)

while current_direction is not None:
  current_location = walk_to_end_of_path(current_direction, current_location)
  current_direction = turn_to_follow_path(current_direction, current_location)

A = "L,12,L,8,R,12"
B = "L,10,L,8,L,12,R,12"
C = "R,12,L,8,L,10"
program = ",".join(map(str,commands))
program = program.replace(A,"A")
program = program.replace(B,"B")
program = program.replace(C,"C")

offset = 0
cmd_num = 0
to_send = program + "\n" + A + "\n" + B + "\n" + C + "\n" + "N" + "\n"
def read_from_keyboard():
  global offset
  offset+=1
  return ord(to_send[offset-1])

memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])
memory[0] = 2
com = Computer(memory)

com.run_program(read_from_keyboard, output_to_screen)