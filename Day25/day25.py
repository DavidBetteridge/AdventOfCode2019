from collections import deque
from Computer import Computer

# Load the program
text = open('Day25/data.txt').read()
s = text.split(',')
memory = {}
for i in range(len(s)):
  memory[i] = int(s[i])

buffer = deque()
def read_from_keyboard():
  if len(buffer) == 0:
    command = input("?")
    for c in command.lower():
      buffer.append(ord(c))
    buffer.append(10)
  return buffer.popleft()

def output_to_screen(valueToPrint):
  print(chr(valueToPrint),end="")


com = Computer(memory)
com.run_program(read_from_keyboard, output_to_screen)


# Items in your inventory:
# - prime number
# - asterisk
# - mutex
# - mug