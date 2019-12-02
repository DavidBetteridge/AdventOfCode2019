from collections import deque
from Computer import Computer

# Load the program
text = open('Day21/data.txt').read()
s = text.split(',')
memory = {}
for i in range(len(s)):
    memory[i] = int(s[i])


input_buffer = deque()
input_buffer.extend("NOT B J\n")
input_buffer.extend("NOT C T\n")
input_buffer.extend("OR J T\n")
input_buffer.extend("AND D T\n")
input_buffer.extend("NOT A J\n")
input_buffer.extend("OR T J\n")
input_buffer.extend("WALK\n")


def read_from_keyboard():
    next = input_buffer.popleft()
    return ord(next)

def output_to_screen(valueToPrint):
    print(chr(valueToPrint),end="")


com = Computer(memory)
com.run_program(read_from_keyboard, output_to_screen)
