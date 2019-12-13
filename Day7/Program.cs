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
            var memory = File.ReadAllText("Part1.txt")
                     .Split(',')
                     .Select(op => int.Parse(op))
                     .ToArray();

            var permutations = GetPermutations(Enumerable.Range(0, 5), 5);

            var bestOutput = int.MinValue;
            var bestPermutation = new int[0];

            foreach (var permutation in permutations)
            {
                var phaseSetting = permutation.ToArray();

                var ampA = new AMP();
                var ampAOutput = ampA.Execute(memory, phaseSetting[0], 0);

                var ampB = new AMP();
                var ampBOutput = ampB.Execute(memory, phaseSetting[1], ampAOutput);

                var ampC = new AMP();
                var ampCOutput = ampC.Execute(memory, phaseSetting[2], ampBOutput);

                var ampD = new AMP();
                var ampDOutput = ampD.Execute(memory, phaseSetting[3], ampCOutput);

                var ampE = new AMP();
                var ampEOutput = ampE.Execute(memory, phaseSetting[4], ampDOutput);

                if (ampEOutput > bestOutput)
                {
                    bestOutput = ampEOutput;
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
