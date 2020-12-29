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

class Computer:

    def __init__(self, memory):
        self.memory = memory

    def read_value_for_parameter_one(self, command, instructionPointer):
        pointer = self.address(instructionPointer + 1, command.parameter1InPositionMode)
        return self.memory[pointer]

    def read_value_for_parameter_two(self, command, instructionPointer):
        pointer = self.address(instructionPointer + 2, command.parameter2InPositionMode)
        return self.memory[pointer]

    def read_address_for_parameter_one(self, instructionPointer):
        return self.memory[instructionPointer + 1]

    def read_address_for_parameter_three(self, instructionPointer):
        return self.memory[instructionPointer + 3]

    def address(self, addressOrValue, isPositionMode):
        if isPositionMode:
            return self.memory[addressOrValue]
        else:
            return addressOrValue

    def run_program(self, inputFunction, outputFunction):
        instructionPointer = 0
        while True:
            command = instruction(self.memory[instructionPointer])

            if command.opCode == OpCode.ADD:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)
                parameter3 = self.read_address_for_parameter_three(instructionPointer)
                self.memory[parameter3] = parameter1 + parameter2
                instructionPointer += 4 

            elif command.opCode == OpCode.MULTIPLY:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)
                parameter3 = self.read_address_for_parameter_three(instructionPointer)
                self.memory[parameter3] = parameter1 * parameter2
                instructionPointer += 4

            elif command.opCode == OpCode.INPUT:
                parameter1 = self.read_address_for_parameter_one(instructionPointer)
                self.memory[parameter1] = inputFunction()
                instructionPointer += 2

            elif command.opCode == OpCode.OUTPUT:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                outputFunction(parameter1)
                instructionPointer += 2

            elif command.opCode == OpCode.JUMP_IF_TRUE:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)

                if parameter1 != 0:
                    instructionPointer = parameter2
                else:
                    instructionPointer += 3

            elif command.opCode == OpCode.JUMP_IF_FALSE:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)
                if parameter1 == 0:
                    instructionPointer = parameter2
                else:
                    instructionPointer += 3

            elif command.opCode == OpCode.LESS_THAN:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)
                parameter3 = self.read_address_for_parameter_three(instructionPointer)
                if parameter1 < parameter2:
                    self.memory[parameter3] = 1
                else:
                    self.memory[parameter3] = 0
                instructionPointer += 4

            elif command.opCode == OpCode.EQUALS:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)
                parameter3 = self.read_address_for_parameter_three(instructionPointer)
                if parameter1 == parameter2:
                    self.memory[parameter3] = 1
                else:
                    self.memory[parameter3] = 0
                instructionPointer += 4

            elif command.opCode == OpCode.HALT:
                break

            else:
                print(f"Error {self.memory[instructionPointer]}")

class CaptureOutput:
    def __init__(self):
        self.captured = ""

    def capture(self, valueToCapture):
        self.captured += str(valueToCapture)

class AMPLink():
    def __init__(self, phaseSetting):
        self.phaseSetting = phaseSetting
        self.value = 0

    def input(self):
        if self.phaseSetting != -1:
            result = self.phaseSetting      
            self.phaseSetting = -1
        else:
            result = self.value
        return result

    def captureOutput(self, value):
        self.value = value     

def output_to_screen(valueToPrint):
    print(valueToPrint, end='')

text = open('Day07/day7.txt').read()
text = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"

bestThrust = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    memoryA = list(map(int, text.split(',')))
                    ampA = Computer(memoryA)
                    linkA = AMPLink(a)

                    memoryB = list(map(int, text.split(',')))
                    ampB = Computer(memoryB)
                    linkB = AMPLink(b)

                    memoryC = list(map(int, text.split(',')))
                    ampC = Computer(memoryC)
                    linkC = AMPLink(c)

                    memoryD = list(map(int, text.split(',')))
                    ampD = Computer(memoryD)
                    linkD = AMPLink(d)

                    memoryE = list(map(int, text.split(',')))
                    ampE = Computer(memoryE)
                    linkE = AMPLink(e)

                    capturer = CaptureOutput()
                    ampA.run_program(linkA.input, capturer.capture)
                    print(capturer.captured)

                    ampB.run_program(linkB.input, linkC.captureOutput)
                    ampC.run_program(linkC.input, linkD.captureOutput)
                    ampD.run_program(linkD.input, linkE.captureOutput)

                    capturer = CaptureOutput()
                    ampE.run_program(linkE.input, capturer.capture)

                    if int(capturer.captured) > bestThrust:
                        bestThrust = int(capturer.captured)
                        print(f'{bestThrust} from {a} {b} {c} {d} {e}')

