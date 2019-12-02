import enum

class OpCode(enum.Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    HALT = 99

class instruction:
    def __init__(self, instruction):
        text = str(instruction)
        self.opCode = OpCode(int(text[-2:]))
        self.parameter1InPositionMode = len(text) < 3 or text[-3] == '0'
        self.parameter2InPositionMode = len(text) < 4 or text[-4] == '0'
        self.parameter3InPositionMode = len(text) < 5 or text[-5] == '0'

def read_value_for_parameter_one(memory, command, instructionPointer):
    pointer = address(memory, instructionPointer + 1, command.parameter1InPositionMode)
    return memory[pointer]

def read_value_for_parameter_two(memory, command, instructionPointer):
    pointer = address(memory, instructionPointer + 2, command.parameter2InPositionMode)
    return memory[pointer]

def read_address_for_parameter_one(memory, instructionPointer):
    return memory[instructionPointer + 1]

def read_address_for_parameter_three(memory, instructionPointer):
    return memory[instructionPointer + 3]

def address(memory, addressOrValue, isPositionMode):
    if isPositionMode:
        return memory[addressOrValue]
    else:
        return addressOrValue

def run_program(memory, inputFunction, outputFunction):
    instructionPointer = 0
    while True:
        command = instruction(memory[instructionPointer])

        if command.opCode == OpCode.ADD:
            parameter1 = read_value_for_parameter_one(memory, command, instructionPointer)
            parameter2 = read_value_for_parameter_two(memory, command, instructionPointer)
            parameter3 = read_address_for_parameter_three(memory, instructionPointer)
            memory[parameter3] = parameter1 + parameter2
            instructionPointer += 4 

        elif command.opCode == OpCode.MULTIPLY:
            parameter1 = read_value_for_parameter_one(memory, command, instructionPointer)
            parameter2 = read_value_for_parameter_two(memory, command, instructionPointer)
            parameter3 = read_address_for_parameter_three(memory, instructionPointer)
            memory[parameter3] = parameter1 * parameter2
            instructionPointer += 4

        elif command.opCode == OpCode.INPUT:
            parameter1 = read_address_for_parameter_one(memory, instructionPointer)
            memory[parameter1] = inputFunction()
            instructionPointer += 2

        elif command.opCode == OpCode.OUTPUT:
            parameter1 = read_value_for_parameter_one(memory, command, instructionPointer)
            outputFunction(parameter1)
            instructionPointer += 2

        elif command.opCode == OpCode.JUMP_IF_TRUE:
            parameter1 = read_value_for_parameter_one(memory, command, instructionPointer)
            parameter2 = read_value_for_parameter_two(memory, command, instructionPointer)

            if parameter1 != 0:
                instructionPointer = parameter2
            else:
                instructionPointer += 3

        elif command.opCode == OpCode.JUMP_IF_FALSE:
            parameter1 = read_value_for_parameter_one(memory, command, instructionPointer)
            parameter2 = read_value_for_parameter_two(memory, command, instructionPointer)
            if parameter1 == 0:
                instructionPointer = parameter2
            else:
                instructionPointer += 3

        elif command.opCode == OpCode.LESS_THAN:
            parameter1 = read_value_for_parameter_one(memory, command, instructionPointer)
            parameter2 = read_value_for_parameter_two(memory, command, instructionPointer)
            parameter3 = read_address_for_parameter_three(memory, instructionPointer)
            if parameter1 < parameter2:
                memory[parameter3] = 1
            else:
                memory[parameter3] = 0
            instructionPointer += 4

        elif command.opCode == OpCode.EQUALS:
            parameter1 = read_value_for_parameter_one(memory, command, instructionPointer)
            parameter2 = read_value_for_parameter_two(memory, command, instructionPointer)
            parameter3 = read_address_for_parameter_three(memory, instructionPointer)
            if parameter1 == parameter2:
                memory[parameter3] = 1
            else:
                memory[parameter3] = 0
            instructionPointer += 4

        elif command.opCode == OpCode.HALT:
            break

        else:
            print(f"Error {memory[instructionPointer]}")

def read_from_keyboard():
    print('?', end='')
    return int(input())

def output_to_screen(valueToPrint):
    print(valueToPrint, end='')

def input_one():
    return 1

def input_five():
    return 5


class CaptureOutput:
    def __init__(self):
        self.captured = ""

    def capture(self, valueToCapture):
        self.captured += str(valueToCapture)

text = open('Day05/day5.txt').read()

def part_one():
    memory = list(map(int, text.split(',')))
    out = CaptureOutput()
    run_program(memory, input_one, out.capture)
    return out.captured

def part_two():
    memory = list(map(int, text.split(',')))
    out = CaptureOutput()
    run_program(memory, input_five, out.capture)
    return out.captured

print(part_one())
print(part_two())
