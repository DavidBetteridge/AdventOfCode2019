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
def output_to_screen(valueToPrint):
  global row
  global column
  
  if valueToPrint == 10:
    row+=1
    column=0
  else:
    grid[(column, row)] = chr(valueToPrint)
    column+=1

  print(chr(valueToPrint),end="")

com = Computer(memory)

com.run_program(read_from_keyboard, output_to_screen)


maxX = max(grid, key=lambda x: x[0])[0]
maxY = max(grid, key=lambda x: x[1])[1]

total = 0
for x in range(1, maxX-1):
  for y in range(1, maxY-1):
    if grid[(x,y)] == "#" and grid[(x+1,y)] == "#" and grid[(x-1,y)] == "#" and grid[(x,y+1)] == "#" and grid[(x,y-1)] == "#":
      total += (x*y)
print(total)      
