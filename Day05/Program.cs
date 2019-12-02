using System.IO;
using System.Linq;

namespace Day5
{
    class Program
    {
        static void Main()
        {
            while (true)
            {
                var memory = File.ReadAllText("day5.txt")
                         .Split(',')
                         .Select(op => int.Parse(op))
                         .ToArray();

                var computer = new Computer(memory);
                computer.RunProgram();
            }
        }
    }
}
