using System;
using System.IO;
using System.Linq;

namespace Day1
{
    class Program
    {
        static void Main()
        {
            static int FuelRequired(int mass)
            {
                var fuel = mass / 3 - 2;
                if (fuel <= 0)
                    return 0;
                else
                    return fuel + FuelRequired(fuel);
            }

            var totalFuel = File.ReadAllLines("Day1.txt")
                                .Select(line => int.Parse(line))
                                .Select(line => FuelRequired(line))
                                .Sum();

            Console.WriteLine(totalFuel);  //4739374
        }
    }
}