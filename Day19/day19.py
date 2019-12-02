from Computer import Computer
from itertools import product

# Load the program
text = open('Day19/data.txt').read()
s = text.split(',')
memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])


def read_from_keyboard():
  global input_no
  if input_no == 0:
    input_no+=1
    return row
  else:
    return column

def output_to_screen(valueToPrint):
  grid[(column, row)] = valueToPrint

grid = {}
for row,column in product(range(50), repeat=2):
  com = Computer(memory.copy())
  input_no = 0
  com.run_program(read_from_keyboard, output_to_screen)

part1 = (sum(p for p in grid.values()))
assert part1 == 129