from Computer import Computer

def read_from_keyboard():
    print('?', end='')
    return int(input())

def output_to_screen(valueToPrint):
    print(valueToPrint, end='')

text = open('Day09/day9.txt').read()

def part_one():
    s = text.split(',')
    memory = {}
    for i in range(len(s)):
        memory[i] = int(s[i])
   
    com = Computer(memory)
    com.run_program(read_from_keyboard, output_to_screen)

part_one()


#2436480432