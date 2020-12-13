from Computer import Computer

def read_from_keyboard():
    print('?', end='')
    return int(input())

def output_to_screen(valueToPrint):
    print(valueToPrint, end='')

x = 0
y = 0
direction = "UP"
paintedPanels = {}

def enter_panel_colour():
    if (x,y) in paintedPanels:
        return paintedPanels[(x,y)]
    else:
        return 0

def turn_right():
    global direction

    if direction == "UP":
        direction = "RIGHT"
    elif direction == "RIGHT":
        direction = "DOWN"
    elif direction == "DOWN":
        direction = "LEFT"
    elif direction == "LEFT":
        direction = "UP"        

def turn_left():
    global direction

    if direction == "UP":
        direction = "LEFT"
    elif direction == "RIGHT":
        direction = "UP"
    elif direction == "DOWN":
        direction = "RIGHT"
    elif direction == "LEFT":
        direction = "DOWN"     

def walk_forward():
    global x
    global y

    if direction == "UP":
        y += 1
    elif direction == "RIGHT":
        x += 1
    elif direction == "DOWN":
        y -= 1
    elif direction == "LEFT":
        x -= 1

colourCommand = True
def handle_commands(command):
    global colourCommand

    if colourCommand == True:
        paintedPanels[(x,y)] = command
        #print(f'Painting {x},{y} with {command}')
    else:
        if command == 1:
            turn_right()
        else:
            turn_left()
        walk_forward()

    colourCommand = not colourCommand        


text = open('Day11/day11.txt').read()
s = text.split(',')
memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])
   

paintedPanels[(x,y)] = 1  # Start on white
com = Computer(memory)
com.run_program(enter_panel_colour, handle_commands)

minX = min(paintedPanels, key=lambda x:x[0])[0]
maxX = max(paintedPanels, key=lambda x:x[0])[0]
minY = min(paintedPanels, key=lambda x:x[1])[1]
maxY = max(paintedPanels, key=lambda x:x[1])[1]

for x in range(minX, maxX + 1):
    row = ""
    for y in range(minY, maxY + 1):
        if (x,y) in paintedPanels and paintedPanels[(x,y)] == 1:
            row += "*"
        else:
            row += " "
    print(row)

#part 1 2418


