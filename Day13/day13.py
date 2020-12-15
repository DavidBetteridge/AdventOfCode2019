from Computer import Computer

class CaptureOutput:
    def __init__(self):
        self.captured = ""

    def capture(self, valueToCapture):
        self.captured += str(valueToCapture) + ","

class Instruction :
    def __init__(self, text):
        self.x = int(text[0])
        self.y = int(text[1])
        self.tileId = int(text[2])

commands = open('Day13/day13.txt').read().split(',')
memory = {}
for i in range(len(commands)):
    memory[i] = int(commands[i])

def read_from_keyboard():
    print('?', end='')
    return int(input())

def output_to_screen(valueToPrint):
    print(valueToPrint, end='')

# Play for free
memory[0] = 2

josephine = CaptureOutput()

com = Computer(memory)
com.run_program(read_from_keyboard, josephine.capture)

captured = josephine.captured[:-1].split(',')

instructions = [Instruction(captured[i:i+3]) for i in range(0, len(captured), 3)]

print(sum([instruction.tileId == 2 for instruction in instructions ]))

#248 high
#1160 high