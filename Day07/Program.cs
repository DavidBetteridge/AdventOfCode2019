using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Day7
{
    class Program
    {
        static void Main()
        {
            var memory = File.ReadAllText("day7.txt")
                     .Split(',')
                     .Select(op => int.Parse(op))
                     .ToArray();

            var permutations = GetPermutations(Enumerable.Range(5, 5), 5);

            var bestOutput = int.MinValue;
            var bestPermutation = new int[0];

            foreach (var permutation in permutations)
            {
                var phaseSetting = permutation.ToArray();

                var input = 0;

                var ampA = new AMP(memory, phaseSetting[0]);
                var ampB = new AMP(memory, phaseSetting[1]);
                var ampC = new AMP(memory, phaseSetting[2]);
                var ampD = new AMP(memory, phaseSetting[3]);
                var ampE = new AMP(memory, phaseSetting[4]);

                while (!ampA.Complete)
                {
                    input = ampA.Execute(input);

                    input = ampB.Execute(input);

                    input = ampC.Execute(input);

                    input = ampD.Execute(input);

                    input = ampE.Execute(input);
                }

                if (input > bestOutput)
                {
                    bestOutput = input;
                    bestPermutation = phaseSetting;
                }
            }

            Console.WriteLine($"{bestOutput} from {bestPermutation[0]},{bestPermutation[1]},{bestPermutation[2]},{bestPermutation[3]},{bestPermutation[4]}");
        }

        static IEnumerable<IEnumerable<T>> GetPermutations<T>(IEnumerable<T> list, int length)
        {
            if (length == 1) return list.Select(t => new T[] { t });

            return GetPermutations(list, length - 1)
                .SelectMany(t => list.Where(e => !t.Contains(e)),
                    (t1, t2) => t1.Concat(new T[] { t2 }));
        }
    }
}
