namespace Day7
{
    public class Instruction
    {
        public int opCode { get; }

        public bool Parameter1InImmediateMode { get; }
        public bool Parameter2InImmediateMode { get; }
        public bool Parameter3InImmediateMode { get; }

        public Instruction(int instruction)
        {
            if (instruction < 100)
            {
                opCode = instruction;
                Parameter1InImmediateMode = false;
                Parameter2InImmediateMode = false;
                Parameter3InImmediateMode = false;
            }
            else
            {
                var txt = instruction.ToString();
                opCode = int.Parse(txt.Substring(txt.Length - 2));
                Parameter1InImmediateMode = txt.Length > 2 && (txt[^3] == '1');
                Parameter2InImmediateMode = txt.Length > 3 && (txt[^4] == '1');
                Parameter3InImmediateMode = txt.Length > 4 && (txt[^5] == '1');
            }
        }
    }
}
