namespace Day7
{
    public class AMP
    {
        private int _result;
        private int _phase;
        private int _nextInput;
        private Computer _computer;
        private bool _phaseSet = false;
        public bool Complete { get; private set; }
        public AMP(int[] memory, int phase)
        {
            _phase = phase;

            _computer = new Computer((int[])memory.Clone(), Input, Output);
        }

        public int Execute(int input)
        {
            _nextInput = input;

            Complete = _computer.RunProgram();

            return _result;
        }

        private int Input()
        {
            if (_phaseSet)
            {
                return _nextInput;
            }
            else
            {
                _phaseSet = true;
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
