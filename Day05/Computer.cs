using System;

namespace Day5
{
    partial class Computer
    {
        private readonly int[] _memory;

        public Computer(int[] memory)
        {
            _memory = memory;
        }

        public void RunProgram()
        {
            var instructionPointer = 0;
            while (_memory[instructionPointer] != 99)
            {
                var instruction = new Instruction(_memory[instructionPointer]);

                instructionPointer = instruction.opCode switch
                {
                    1 => ADD(instructionPointer, instruction),
                    2 => MUL(instructionPointer, instruction),
                    3 => INPUT(instructionPointer, instruction),
                    4 => OUTPUT(instructionPointer, instruction),
                    5 => JMP_IF_TRUE(instructionPointer, instruction),
                    6 => JMP_IF_FALSE(instructionPointer, instruction),
                    7 => JMP_IF_LESS_THAN(instructionPointer, instruction),
                    8 => JMP_IF_EQUALS(instructionPointer, instruction),
                    _ => throw new System.Exception($"Unexpected opcode {instruction.opCode}")
                };

            }
        }
        private int JMP_IF_EQUALS(int instructionPointer, Instruction instruction)
        {
            var value1 = ReadMemory(instructionPointer + 1, instruction.Parameter1InImmediateMode);
            var value2 = ReadMemory(instructionPointer + 2, instruction.Parameter2InImmediateMode);
            var address3 = _memory[instructionPointer + 3];

            if (value1 == value2)
                _memory[address3] = 1;
            else
                _memory[address3] = 0;

            return instructionPointer + 4;
        }

        private int JMP_IF_LESS_THAN(int instructionPointer, Instruction instruction)
        {
            var value1 = ReadMemory(instructionPointer + 1, instruction.Parameter1InImmediateMode);
            var value2 = ReadMemory(instructionPointer + 2, instruction.Parameter2InImmediateMode);
            var address3 = _memory[instructionPointer + 3];

            if (value1 < value2)
                _memory[address3] = 1;
            else
                _memory[address3] = 0;

            return instructionPointer + 4;
        }

        private int JMP_IF_FALSE(int instructionPointer, Instruction instruction)
        {
            var value1 = ReadMemory(instructionPointer + 1, instruction.Parameter1InImmediateMode);
            if (value1 == 0)
            {
                var newInstructionPointer = ReadMemory(instructionPointer + 2, instruction.Parameter2InImmediateMode);
                return newInstructionPointer;
            }

            return instructionPointer + 3;
        }

        private int JMP_IF_TRUE(int instructionPointer, Instruction instruction)
        {
            var value1 = ReadMemory(instructionPointer + 1, instruction.Parameter1InImmediateMode);
            if (value1 != 0)
            {
                var newInstructionPointer = ReadMemory(instructionPointer + 2, instruction.Parameter2InImmediateMode);
                return newInstructionPointer;
            }

            return instructionPointer + 3;
        }

        private int ReadMemory(int address, bool immediateMode)
        {
            var location = immediateMode ? address : _memory[address];
            return _memory[location];
        }

        private int ADD(int instructionPointer, Instruction instruction)
        {
            var value1 = ReadMemory(instructionPointer + 1, instruction.Parameter1InImmediateMode);
            var value2 = ReadMemory(instructionPointer + 2, instruction.Parameter2InImmediateMode);
            var address3 = _memory[instructionPointer + 3];

            _memory[address3] = value1 + value2;

            return instructionPointer + 4;
        }

        private int MUL(int instructionPointer, Instruction instruction)
        {
            var value1 = ReadMemory(instructionPointer + 1, instruction.Parameter1InImmediateMode);
            var value2 = ReadMemory(instructionPointer + 2, instruction.Parameter2InImmediateMode);
            var address3 = _memory[instructionPointer + 3];

            _memory[address3] = value1 * value2;

            return instructionPointer + 4;
        }

        private int INPUT(int instructionPointer, Instruction instruction)
        {
            var address1 = _memory[instructionPointer + 1];

            Console.Write("> ");
            var input = int.Parse(Console.ReadLine());

            _memory[address1] = input;

            return instructionPointer + 2;
        }

        private int OUTPUT(int instructionPointer, Instruction instruction)
        {
            var output = ReadMemory(instructionPointer + 1, instruction.Parameter1InImmediateMode);

            Console.WriteLine(output);

            return instructionPointer + 2;
        }
    }
}
