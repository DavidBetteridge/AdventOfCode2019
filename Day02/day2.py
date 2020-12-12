text = open('Day02/day2.txt').read()

def run_program(memory):
    instructionPointer = 0
    while memory[instructionPointer] != 99:
        if memory[instructionPointer] == 1:
            address1 = memory[instructionPointer + 1]
            address2 = memory[instructionPointer + 2]
            address3 = memory[instructionPointer + 3]
            memory[address3] = memory[address1] + memory[address2]
            instructionPointer += 4 

        elif memory[instructionPointer] == 2:
            address1 = memory[instructionPointer + 1]
            address2 = memory[instructionPointer + 2]
            address3 = memory[instructionPointer + 3]
            memory[address3] = memory[address1] * memory[address2]
            instructionPointer += 4

        else:
            print(f"Error {memory[instructionPointer]}")

def part_one():
    memory = list(map(int, text.split(',')))
    memory[1] = 12
    memory[2] = 2
    run_program(memory)
    return memory[0]

def part_two():
    for noun in range(0, 100):
        for verb in range(0, 100):
            memory = list(map(int, text.split(',')))
            memory[1] = noun
            memory[2] = verb
            run_program(memory)
            if memory[0] == 19690720:
                return 100 * noun + verb
                
print(part_one())                
print(part_two())                

input()
