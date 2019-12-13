using Day5;
using System;

namespace Day7
{
    public class AMP
    {
        private int _result;
        private int _phase;
        private int _input;
        private Computer _computer;
        private bool secondInput = false;

        public int Execute(int[] memory, int phase, int input)
        {
            _phase = phase;
            _input = input;

            _computer = new Computer((int[])memory.Clone(), Input, Output);
            _computer.RunProgram();

            return _result;
        }

        private int Input()
        {
            if (secondInput)
            {
                return _input;
            }
            else
            {
                secondInput = true;
                return _phase;
            }
        }

        private void Output(int value)
        {
           // Console.Write(value);
            _result = value;
            _computer.Halt();
        }
    }
}
