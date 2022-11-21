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
    ADJUST_RELATIVE_BASE = 9
    HALT = 99

class ParameterMode(enum.Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class instruction:
    def __init__(self, instruction):
        text = str(instruction)
        self.opCode = OpCode(int(text[-2:]))

        if len(text) < 3:
            self.parameter1Mode = ParameterMode.POSITION
        else:              
            self.parameter1Mode = ParameterMode(int(text[-3]))

        if len(text) < 4:
            self.parameter2Mode = ParameterMode.POSITION
        else:              
            self.parameter2Mode = ParameterMode(int(text[-4]))

        if len(text) < 5:
            self.parameter3Mode = ParameterMode.POSITION
        else:              
            self.parameter3Mode = ParameterMode(int(text[-5]))            

class Computer:

    def __init__(self, memory):
        self.memory = memory
        self.relativeBase = 0

    def read_value_for_parameter_one(self, command, instructionPointer):
        pointer = self.address(instructionPointer + 1, command.parameter1Mode)
        if pointer in self.memory:
            return self.memory[pointer]
        else:
            return 0

    def read_value_for_parameter_two(self, command, instructionPointer):
        pointer = self.address(instructionPointer + 2, command.parameter2Mode)
        if pointer in self.memory:
            return self.memory[pointer]
        else:
            return 0

    def read_address_for_parameter_one(self, command, instructionPointer):
        if command.parameter1Mode == ParameterMode.POSITION:
            return self.memory[instructionPointer + 1]
        elif command.parameter1Mode == ParameterMode.RELATIVE:
            return self.memory[instructionPointer + 1] + self.relativeBase     
        else:
            raise Exception(f"parameterMode must be POSITION or RELATIVE.  Not {command.parameter3Mode}.") 

    def read_address_for_parameter_three(self, command, instructionPointer):
        if command.parameter3Mode == ParameterMode.POSITION:
            return self.memory[instructionPointer + 3]
        elif command.parameter3Mode == ParameterMode.RELATIVE:
            return self.memory[instructionPointer + 3] + self.relativeBase     
        else:
            raise Exception(f"parameterMode must be POSITION or RELATIVE.  Not {command.parameter3Mode}.")                

    def address(self, addressOrValue, parameterMode):
        if parameterMode == ParameterMode.POSITION:
            return self.memory[addressOrValue]
        elif parameterMode == ParameterMode.IMMEDIATE:            
            return addressOrValue
        elif parameterMode == ParameterMode.RELATIVE:                        
            return self.memory[addressOrValue] + self.relativeBase
        else:
            raise Exception(f"parameterMode must be POSITION, IMMEDIATE or RELATIVE.  Not {parameterMode}.")

    def run_program(self, inputFunction, outputFunction):
        instructionPointer = 0
        while True:
            command = instruction(self.memory[instructionPointer])

            if command.opCode == OpCode.ADD:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)
                parameter3 = self.read_address_for_parameter_three(command, instructionPointer)
                self.memory[parameter3] = parameter1 + parameter2
                instructionPointer += 4 

            elif command.opCode == OpCode.MULTIPLY:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)
                parameter3 = self.read_address_for_parameter_three(command, instructionPointer)
                self.memory[parameter3] = parameter1 * parameter2
                instructionPointer += 4

            elif command.opCode == OpCode.INPUT:
                parameter1 = self.read_address_for_parameter_one(command, instructionPointer)
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
                parameter3 = self.read_address_for_parameter_three(command, instructionPointer)
                if parameter1 < parameter2:
                    self.memory[parameter3] = 1
                else:
                    self.memory[parameter3] = 0
                instructionPointer += 4

            elif command.opCode == OpCode.EQUALS:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                parameter2 = self.read_value_for_parameter_two(command, instructionPointer)
                parameter3 = self.read_address_for_parameter_three(command, instructionPointer)
                if parameter1 == parameter2:
                    self.memory[parameter3] = 1
                else:
                    self.memory[parameter3] = 0
                instructionPointer += 4

            elif command.opCode == OpCode.ADJUST_RELATIVE_BASE:
                parameter1 = self.read_value_for_parameter_one(command, instructionPointer)
                self.relativeBase += parameter1
                instructionPointer += 2

            elif command.opCode == OpCode.HALT:
                break

            else:
                print(f"Error {self.memory[instructionPointer]}")