using System;
using System.IO;
using System.Linq;

namespace Day2
{
    class Program
    {
        static void Main()
        {
            for (int noun = 0; noun < 100; noun++)
            {
                for (int verb = 0; verb < 100; verb++)
                {
                    if (RunProgram(noun, verb) == 19690720)
                    {
                        Console.WriteLine(100 * noun + verb);
                    }
                }
            }
        }

        private static int RunProgram(int noun, int verb)
        {
            var memory = File.ReadAllText("Day2.txt")
                             .Split(',')
                             .Select(op => int.Parse(op))
                             .ToArray();

            memory[1] = noun;
            memory[2] = verb;

            var instructionPointer = 0;
            while (memory[instructionPointer] != 99)
            {
                var opCode = memory[instructionPointer];
                var address1 = memory[instructionPointer + 1];
                var address2 = memory[instructionPointer + 2];
                var address3 = memory[instructionPointer + 3];

                if (opCode == 1)
                {
                    memory[address3] = memory[address1] + memory[address2];
                }

                if (opCode == 2)
                {
                    memory[address3] = memory[address1] * memory[address2];
                }

                instructionPointer += 4;
            }

            return memory[0];
        }
    }
}
